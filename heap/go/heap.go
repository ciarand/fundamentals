package heap

import (
	"sync"
)

// Heap is a heap implementation in Go.
type Heap struct {
	data   []int
	cursor int

	lock sync.RWMutex
}

// NewHeap creates a new Heap structure.
func NewHeap() *Heap {
	// capacity of 1 for fun
	return &Heap{make([]int, 1), 0, sync.RWMutex{}}
}

// Insert adds a new value into the Heap.
func (h *Heap) Insert(c int) {
	h.lock.Lock()
	defer h.lock.Unlock()

	if hlen := len(h.data); hlen <= h.cursor {
		h.grow(2)
	}

	h.data[h.cursor] = c
	h.cursor++

	h.heapifyUp(h.cursor - 1)
}

// Remove deletes the smallest value from the Heap and returns it.
func (h *Heap) Remove() int {
	h.lock.Lock()
	defer h.lock.Unlock()

	ret := h.data[0]

	h.data[0] = h.data[h.cursor-1]
	h.cursor--

	h.heapifyDown(0)

	return ret
}

// Peek returns the smallest value in the Heap.
func (h *Heap) Peek() int {
	h.lock.RLock()
	defer h.lock.RUnlock()

	return h.data[0]
}

// grow increases the size of the backing array by a factor of rate.
func (h *Heap) grow(rate int) {
	newdata := make([]int, len(h.data)*rate)
	copy(newdata, h.data)
	h.data = newdata
}

// parent returns the index to the parent of the provided node index (i).
func (h *Heap) parent(i int) int {
	return (i - 1) / 2
}

// kthChild returns the index to the Kth child of the provided node index (i).
func (h *Heap) kthChild(i int, k int) int {
	return 2*i + k
}

// minChild returns the index that represents the smallest child of the provided node index (i).
func (h *Heap) minChild(i int) int {
	lc, rc := h.kthChild(i, 1), h.kthChild(i, 2)

	if h.data[lc] < h.data[rc] {
		return lc
	} else {
		return rc
	}
}

func (h *Heap) heapifyUp(childKey int) {
	tmp := h.data[childKey]

	// while the child index isn't 0 (the top) and while the child elem is
	// smaller than the parent elem
	for parentKey := h.parent(childKey); childKey > 0 && tmp < h.data[parentKey]; parentKey = h.parent(childKey) {
		h.data[childKey] = h.data[parentKey]
		childKey = parentKey
	}

	h.data[childKey] = tmp
}

func (h *Heap) heapifyDown(parentKey int) {
	tmp := h.data[parentKey]

	for h.kthChild(parentKey, 1) < h.cursor {
		child := h.minChild(parentKey)

		if h.data[child] < tmp {
			h.data[parentKey] = h.data[child]
		} else {
			break
		}

		parentKey = child
	}

	h.data[parentKey] = tmp
}
