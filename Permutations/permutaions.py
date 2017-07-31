#!/usr/bin/python
# coding=utf-8
#
# Title:    Permutations
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-07-31 22:46:23
#
"""
Recursive Solution 

Beats 76.32% 
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        ret = []
        for i in range(len(nums)):
            nums_except_i = nums[:i] + nums[i+1:]
            for j in self.permute(nums_except_i):
                ret.append([nums[i]]+j)
        return ret
