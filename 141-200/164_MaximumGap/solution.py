#!/usr/bin/env python
# coding=utf-8
#
# Title: 164 Maximum Gap
# Author: Lucas
# Date: 2018-05-29 21:37:41
#
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums = sorted(nums)
        max_diff = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > max_diff:
                max_diff = nums[i+1] - nums[i]
        return max_diff
