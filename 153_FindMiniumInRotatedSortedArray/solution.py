#!/usr/bin/env python
# coding=utf-8
#
# Title: 153. Find Minimum in Rotated Sorted Array
# Author: Lucas
# Date: 2018-05-24 20:08:23
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(nums)
        return self._helper(nums, 0, len(nums)-1)

    def _helper(self, nums, start, end):
        if start == end:
            return nums[start]
        if end - start < 2:
            return min(nums[start], nums[end])

        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            return self._helper(nums, mid, end)
        return self._helper(nums, start, mid)
