#!/usr/bin/env python3


class MaxHeap(object):
    def __init__(self, heap=None):
        self.heap = [] if heap is None else heap.copy()
        self.size = len(heap)

    def __eq__(self, other=None):
        if other and isinstance(other, MaxHeap) and \
           self.size == other.size and \
           self.heap[:self.size] == other.heap[:other.size]:
            return True
        return False

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

    def get_parent_index(self, index):
        if index == 0 or index > self.size:
            return
        parent_index = int((index - 1) / 2)
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

    @staticmethod
    def max_heap_sort(data):
        if isinstance(data, list):
            heap = MaxHeap(heap=data)
            return heap.__max_heap_sort()
        elif isinstance(data, MaxHeap):
            heap_data = data.heap
            heap_size = data.size
            return MaxHeap.max_heap_sort(heap_data[:heap_size])
        else:
            raise TypeError("cannot sort type other than list or MaxHeap")

    def __max_heap_sort(self):
        result_list = []
        self.build_max_heap()
        for i in range(self.size):
            result_list.append(self.heap[0])

            self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
            self.size -= 1
            self.max_heapify(index=0)

        return result_list

    def maximum(self):
        return self.heap[0] if self.size > 0 else None

    def extract_maximum(self):
        if self.size == 0:
            return
        max_res = self.heap[0]

        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.max_heapify(index=0)
        return max_res

    def value_change(self, index, new_value, insert=False):
        if index >= self.size:
            return
        old_value = self.heap[index]

        # if insert is True, ignore index
        if insert:
            index = self.size - 1

        if new_value > old_value or insert:
            old_index = index
            new_index = self.get_parent_index(old_index)
            while new_index is not None:
                if self.heap[new_index] < new_value:
                    self.heap[old_index] = self.heap[new_index]
                    old_index = new_index
                    new_index = self.get_parent_index(old_index)
                else:
                    break
            self.heap[old_index] = new_value
        elif new_value < old_value:
            self.heap[index] = new_value
            self.max_heapify(index=index)

    def insert(self, value):
        if len(self.heap) == self.size:
            self.heap.append(value)
        else:
            self.heap[self.size] = value

        self.size += 1
        self.value_change(0, value, insert=True)