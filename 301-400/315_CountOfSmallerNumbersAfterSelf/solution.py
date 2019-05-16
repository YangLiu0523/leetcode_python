#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-16 20:41:15
"""
Add steps to record move in merge sort
"""
from typing import List


class Solution:
    def __init__(self):
        self.aux = None
        self.aux_count = None

    def _merge(self, nums, start, mid, end, count):
        index = start
        s1 = start
        s2 = mid
        while index < end:
            if s1 >= mid:
                self.aux[index] = nums[s2]
                self.aux_count[index] = count[s2]
                s2 += 1
            elif s2 >=end:
                self.aux[index] = nums[s1]
                self.aux_count[index] = count[s1] + s2 - mid
                # count[nums[s1]] += s2 - mid
                s1 += 1
            elif nums[s1] <= nums[s2]:
                self.aux[index] = nums[s1]
                self.aux_count[index] = count[s1] + s2 - mid
                # count[nums[s1]] += s2 - mid
                s1 += 1
            else:
                self.aux[index] = nums[s2]
                self.aux_count[index] = count[s2]
                s2 += 1
            index += 1

        for i in range(start, end):
            nums[i] = self.aux[i]
            count[i] = self.aux_count[i]

    def _mergesort(self, nums, start, end, count):
        if end - start <= 1:
            return

        mid = (start + end) // 2
        self._mergesort(nums, start, mid, count)
        self._mergesort(nums, mid, end, count)
        self._merge(nums, start, mid, end, count)

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.aux = [0] * len(nums)
        self.aux_count = [0] * len(nums)
        copy_nums = nums[:]
        count = [0] * len(nums)
        # count = {k:0 for k in nums}
        self._mergesort(copy_nums, 0, len(nums), count)

        tmp = [(i, nums[i]) for i in range(len(nums))]
        tmp.sort(key=lambda x: x[1])
        ans = [0] * len(nums)
        for i in range(len(tmp)):
            prev_i = tmp[i][0]
            ans[prev_i] = count[i]
        return ans


def main():
    testcases = [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        (
            [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41],
            [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
        )
    ]
    for case, target in testcases:
        ans = Solution().countSmaller(case)
        assert ans == target, "\n%s != \n%s" % (ans, target)


if __name__ == '__main__':
    main()
