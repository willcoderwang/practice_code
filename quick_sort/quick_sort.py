#!/usr/bin/env python3


def quick_sort(nums, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(nums) - 1

    if end <= start:
        return

    head = start
    tail = end

    while tail > head:
        while tail > head and nums[tail] > nums[head]:
            tail -= 1
        else:
            if tail == head:
                quick_sort(nums, start, tail-1)
                quick_sort(nums, tail+1, end)
                return
            else:
                nums[head], nums[tail] = nums[tail], nums[head]

        while head < tail and nums[head] < nums[tail]:
            head += 1
        else:
            if tail == head:
                quick_sort(nums, start, tail-1)
                quick_sort(nums, tail+1, end)
                return
            else:
                nums[head], nums[tail] = nums[tail], nums[head]
