class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def get_size(self):
        return len(self.heap)

    def get_left_child_index(self, index=0):
        left_child_index = index * 2 + 1
        if left_child_index < len(self.heap):
            return left_child_index

    def get_right_child_index(self, index=0):
        right_child_index = index * 2 + 2
        if right_child_index < len(self.heap):
            return right_child_index

    def get_parent_child_index(self, index):
        if index == 0:
            return
        parent_index = (index - 1) / 2
        if parent_index < len(self.heap):
            return parent_index
