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

Beats 98% 
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        result = []
        for perm in self.permute(nums[1:]):
            for i in xrange(len(perm) + 1):
                result.append(perm[:i] + [nums[0]] + perm[i:])
        return result
