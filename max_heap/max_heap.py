#!/usr/bin/env python3


class MaxHeap(object):
    def __init__(self, heap=None):
        self.heap = [] if heap is None else heap
        self.size = len(heap)

    def __repr__(self):
        return str(self.heap)

    def build_max_heap(self):
        start_point = int((self.size - 1) / 2)
        for i in reversed(range(start_point)):
            self.max_heapify(i)

    def get_left_child_index(self, index=0):
        left_child_index = index * 2 + 1
        if left_child_index < self.size:
            return left_child_index

    def get_right_child_index(self, index=0):
        right_child_index = index * 2 + 2
        if right_child_index < self.size:
            return right_child_index

    def has_child(self, index=0):
        if not self.get_left_child_index(index) and \
           not self.get_right_child_index(index):
            return False

        return True

    def get_parent_child_index(self, index):
        if index == 0 or index > self.size:
            return
        parent_index = (index - 1) / 2
        return parent_index

    def max_heapify(self, index):
        largest = index

        left_child_index = self.get_left_child_index(index)
        if left_child_index and \
           self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        right_child_index = self.get_right_child_index(index)
        if right_child_index and \
           self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)
