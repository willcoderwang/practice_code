#!/user/bin/env python3
import unittest
from quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        nums = [2, 8, 7, 1, 3, 5, 6, 4]
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8]
        quick_sort(nums)
        self.assertEqual(nums, sorted_nums)


if __name__ == '__main__':
    unittest.main()