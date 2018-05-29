#!/usr/bin/env python
# coding=utf-8
#
# Title: 162. Find Peak Element
# Author: Lucas
# Date: 2018-05-29 21:35:09
#
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i-1]:
                continue
            if i < len(nums) - 1 and nums[i] <= nums[i+1]:
                continue
            return i
