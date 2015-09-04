#!/usr/bin/env python3

import unittest

class Heap:
    hsize = 0
    data = []

    def insert(self, item):
        " Adds a new element to the heap "
        self.data[self.hsize] = item
        self.hsize += 1
        heapify_up(self.hsize - 1)

    def remove(self):
        "Removes the first (minimum) item from the heap and returns it"
        if self.hsize == 0:
            raise Exception("underflow, no items left to remove")

        subject = self.data[0]
        self.hsize -= 1
        self.data = self.data[1:]

        if self.hsize > 0:
            heapify_down(0)

        return subject

    def heapify_up(self, index):
        subject = self.data[index]
        parent_index = self.index_of_parent(index)

        while self.data[parent_index] > subject:
            self.data[index] = self.data[parent_index]
            index = parent_index
            parent = self.index_of_parent(index)

        self.data[index] = subject

    def heapify_down(self, index):
        subject = data[index]
        child_index = self.min_child(index)
        while data[index] > data[child_index]:
            data[index] = data[child_index]
            index = child_index
            child_index = self.min_child(index)

        data[index] = subject

    def index_of_parent(self, child_index):
        return (child_index - 1) // 2

    def min_child(self, parent_index):
        lc = 2 * parent_index + 1
        rc = 2 * parent_index + 2

        return lc if self.data[lc] < self.data[rc] else rc

class TestHeap(unittest.TestCase):
    def test_removes_in_order(self):
        h = Heap()
        limit = 10000

        # prepop (but backwards)
        (h.insert(x) for x in range(0, limit, -1))

        # they should be removed in order
        (self.assertEqual(x, h.remove()) for x in range(0, limit, -1))

    def test_always_keeps_internal_state_in_order(self):
        h = Heap()
        limit = 10000

        # prepop
        (h.insert(x) for x in range(limit))

        for x in range(1, limit, -1):
            self.assertEqual(x, h.data[0])
            self.assertEqual(x, h.remove())

            self.assertEqual(x - 1, h.data[0])

if __name__ == "__main__":
    unittest.main()
