package main

import (
	"bytes"
	"hash/crc64"
)

type HashTable struct {
	data [][]keyValue
}

type keyValue struct {
	key   []byte
	value interface{}
}

func NewHashTable(ln int) *HashTable {
	return &HashTable{make([][]keyValue, ln)}
}

func (h *HashTable) Set(k []byte, v interface{}) {
	hashk := h.hash(k)

	if h.data[hashk] == nil {
		h.data[hashk] = []keyValue{keyValue{k, v}}
		return
	}

	if found, i := h.find(h.data[hashk], k); found {
		h.data[hashk][i] = keyValue{k, v}
		return
	}

	h.data[hashk] = append(h.data[hashk], keyValue{k, v})
}

func (h *HashTable) Get(k []byte) interface{} {
	hashk := h.hash(k)
	bucket := h.data[hashk]
	if bucket == nil {
		return nil
	}

	if exists, i := h.find(bucket, k); exists {
		return bucket[i].value
	}

	return nil
}

func (h *HashTable) find(bucket []keyValue, k []byte) (bool, int) {
	for i, elem := range bucket {
		if bytes.Equal(k, elem.key) {
			return true, i
		}
	}

	return false, 0
}

func (h *HashTable) hash(k []byte) uint64 {
	hash := crc64.New(crc64.MakeTable(crc64.ISO))

	_, _ = hash.Write(k)

	return hash.Sum64() % uint64(len(h.data))
}
