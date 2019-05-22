#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-22 21:27:21
"""
Using Greedy
"""


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        achieved = 0
        index = 0
        while achieved < n:
            target = achieved + 1
            if index < len(nums) and nums[index] <= target:
                achieved += nums[index]
                index += 1
            else:
                achieved += target
                ans += 1
        return ans
