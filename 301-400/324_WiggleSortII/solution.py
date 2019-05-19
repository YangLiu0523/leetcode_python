#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-19 19:28:32


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:]
        tmp.sort()
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1

        for i in range(n):

            if i % 2 == 0:
                nums[i] = tmp[left]
                left -= 1
            else:
                nums[i] = tmp[right]
                right -= 1
