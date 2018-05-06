#!/usr/bin/env python3
import max_heap
import unittest
import copy


class TestMaxHeapMethods(unittest.TestCase):

    def test_max_heapify(self):
        data = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        heap = max_heap.MaxHeap(heap=data)
        heap.max_heapify(1)
        expected_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        expected_heap = max_heap.MaxHeap(heap=expected_data)
        self.assertEqual(heap, expected_heap)

    def test_build_max_heap(self):
        data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        heap = max_heap.MaxHeap(heap=data)
        heap.build_max_heap()
        expected_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        expected_heap = max_heap.MaxHeap(heap=expected_data)
        self.assertEqual(heap, expected_heap)

    def test_max_heap_sort(self):
        data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        expected_sorted_data = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
        sorted_data = max_heap.MaxHeap.max_heap_sort(data)
        self.assertEqual(sorted_data, expected_sorted_data)

        # check if data value is changed
        self.assertEqual(data, [4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

        heap = max_heap.MaxHeap(heap=data)
        heap_cp = copy.deepcopy(heap)
        sorted_data = max_heap.MaxHeap.max_heap_sort(heap)
        self.assertEqual(sorted_data, expected_sorted_data)

        # check if heap is changed
        self.assertEqual(heap, heap_cp)

    def test_maximum_and_extract_maximum(self):
        max_heap_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        max_heap_inst = max_heap.MaxHeap(heap=max_heap_data)
        self.assertEqual(max_heap_inst.maximum(), 16)
        self.assertEqual(max_heap_inst.extract_maximum(), 16)
        self.assertEqual(max_heap_inst.maximum(), 14)

    def test_value_change(self):
        pre_heap_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        pre_heap = max_heap.MaxHeap(heap=pre_heap_data)

        # no change
        pre_heap.value_change(index=2, new_value=10)
        self.assertEqual(pre_heap, max_heap.MaxHeap(heap=pre_heap_data))

        # value increase, index 4 increase from 7 to 30
        incr_heap_data = [30, 16, 10, 8, 14, 9, 3, 2, 4, 1]
        incr_heap = max_heap.MaxHeap(heap=incr_heap_data)
        pre_heap.value_change(index=4, new_value=30)
        self.assertEqual(pre_heap, incr_heap)

        # value decrease, index 0 decrease from 16 to 0
        pre_heap = max_heap.MaxHeap(heap=pre_heap_data)
        decr_heap_data = [14, 8, 10, 4, 7, 9, 3, 2, 0, 1]
        decr_heap = max_heap.MaxHeap(heap=decr_heap_data)
        pre_heap.value_change(index=0, new_value=0)
        self.assertEqual(pre_heap, decr_heap)

    def test_insert(self):
        pre_heap_data = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        pre_heap = max_heap.MaxHeap(heap=pre_heap_data)
        pre_heap.insert(18)
        expected_heap_data = [18, 16, 10, 8, 14, 9, 3, 2, 4, 1, 7]
        expected_heap = max_heap.MaxHeap(expected_heap_data)
        self.assertEqual(pre_heap, expected_heap)

        pre_heap.insert(0)
        expected_heap_data2 = [18, 16, 10, 8, 14, 9, 3, 2, 4, 1, 7, 0]
        expected_heap2 = max_heap.MaxHeap(expected_heap_data2)
        self.assertEqual(pre_heap, expected_heap2)


if __name__ == '__main__':
    unittest.main()
