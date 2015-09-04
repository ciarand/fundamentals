#!/usr/bin/env python
# vim: set fileencoding=utf8 :

import unittest

class HashTable:
    def __init__(self, capacity):
        self.data = [[] for x in xrange(capacity)]
        self.length = capacity

    def set(self, key, value):
        self.data[self.hash(key)].append((key, value))

    def get(self, key):
        for candidate in self.data[self.hash(key)]:
            k, v = candidate

            if k == key:
                return v

        return None

    def hash(self, value):
        return hash(value) % self.length

class TestHashTable(unittest.TestCase):
    def test_hash_table(self):
        h = HashTable(300)

        opinion = "ಠ_ಠ"

        h.set("# of problems", 99)
        h.set("# of bottles", 99)
        h.set("opinion on all this", opinion)
        h.set(0, opinion)
        h.set(1, hash(opinion))

        self.assertEqual(99, h.get("# of problems"))
        self.assertEqual(99, h.get("# of bottles"))
        self.assertEqual(opinion, h.get("opinion on all this"))
        self.assertEqual(opinion, h.get(0))
        self.assertEqual(hash(opinion), h.get(1))

        self.assertIsNone(h.get("nothing here yo"))

if __name__ == "__main__":
    unittest.main()
