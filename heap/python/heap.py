#!/usr/bin/env python3

import unittest

class Heap:
    def __init__(self):
        self.data = []

    def insert(self, item):
        " Adds a new element to the heap "
        self.data.append(item)
        self.heapify_up(len(self.data) - 1)

    def remove(self):
        "Removes the first (minimum) item from the heap and returns it"
        if len(self.data) == 0:
            raise Exception("underflow, no items left to remove")

        subject = self.data[0]
        self.data = self.data[1:]

        if len(self.data) > 0:
            self.heapify_down(0)

        return subject

    def heapify_up(self, index):
        "Resorts the heap, starting from the bottom"
        if (index + 1) > len(self.data):
            raise OverflowError()
        if index < 0:
            raise Exception()

        subject = self.data[index]
        parent_index = self.index_of_parent(index)

        while parent_index >= 0 and self.data[parent_index] > subject:
            self.data[index] = self.data[parent_index]
            index = parent_index
            parent_index = self.index_of_parent(index)

        self.data[index] = subject

    def heapify_down(self, index):
        "Resorts the heap, starting from the top"
        subject = self.data[index]
        child_index = self.min_child(index)

        while child_index != None and self.data[index] > self.data[child_index]:
            self.data[index] = self.data[child_index]
            index = child_index
            child_index = self.min_child(index)

        self.data[index] = subject

    def index_of_parent(self, child_index):
        "Returns the index of the parent"
        return (child_index - 1) // 2

    def min_child(self, parent_index):
        "Returns the index of the smallest child, or None if there are no children"
        lc = 2 * parent_index + 1
        rc = 2 * parent_index + 2

        if lc > len(self.data) - 1:
            return None

        if rc > len(self.data) - 1:
            return lc

        return lc if self.data[lc] < self.data[rc] else rc

class TestHeap(unittest.TestCase):
    def test_removes_in_order(self):
        limit = 10000

        # make sure they maintain separate storage
        heaps = [Heap(), Heap(), Heap(), Heap(), Heap()]
        for h in heaps:
            self.assertEqual(0, len(h.data))
            # prepop (but backwards)
            for x in range(limit, 0, -1): h.insert(x)

        for h in heaps:
            self.assertEqual(limit, len(h.data))
            # they should be removed in order
            for x in range(0, limit, -1):
                self.assertEqual(x, h.remove())

    def test_always_keeps_internal_state_in_order(self):
        h = Heap()
        limit = 10000

        # prepop
        for x in range(limit):
            h.insert(x)

        for x in range(0, limit - 1):
            self.assertEqual(x, h.data[0])
            self.assertEqual(x, h.remove())
            self.assertEqual(x + 1, h.data[0])

if __name__ == "__main__":
    unittest.main()
