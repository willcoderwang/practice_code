#!/usr/bin/env python3
import max_heap
import unittest


class TestMaxHeapMethods(unittest.TestCase):

    def test_max_heapify(self):
        data = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        heap = max_heap.MaxHeap(heap=data)
        heap.max_heapify(1)
        expected_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        expected_heap = max_heap.MaxHeap(heap=expected_data)
        self.assertEqual(repr(heap), repr(expected_heap))

    def test_build_max_heap(self):
        data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        heap = max_heap.MaxHeap(heap=data)
        heap.build_max_heap()
        expected_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        expected_heap = max_heap.MaxHeap(heap=expected_data)
        self.assertEqual(repr(heap), repr(expected_heap))


if __name__ == '__main__':
    unittest.main()
