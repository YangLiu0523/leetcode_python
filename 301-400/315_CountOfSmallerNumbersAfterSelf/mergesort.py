#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-16 08:18:42
"""
One method to solve the problem No.315 is to use merge sort. So just implement
merge sort here and try to find the relation between merge sort and this
problem.
"""


def _merge(nums, start, mid, end, aux):
    s1 = start
    s2 = mid
    index = start
    while index < end:
        if s1 == mid:
            aux[index] = nums[s2]
            s2 += 1
        elif s2 == end:
            aux[index] = nums[s1]
            s1 += 1
        elif nums[s1] > nums[s2]:
            aux[index] = nums[s2]
            s2 += 1
        else:
            aux[index] = nums[s1]
            s1 += 1
        index += 1

    for i in range(start, end):
        nums[i] = aux[i]


def _mergesort(nums, start, end, aux):
    if end - start <= 1:
        return

    mid = (start + end) // 2
    _mergesort(nums, start, mid, aux)
    _mergesort(nums, mid, end, aux)
    _merge(nums, start, mid, end, aux)


def mergesort(nums):
    aux = [0] * len(nums)
    _mergesort(nums, 0, len(nums), aux)


# Testcases
def main():
    testcases = [
        [3, 5, 2, 4, 1]
    ]
    for case in testcases:
        sorted_nums = sorted(case)
        mergesort(case)
        assert sorted_nums == case, "%s != %s" % (sorted_nums, case)


if __name__ == '__main__':
    main()
