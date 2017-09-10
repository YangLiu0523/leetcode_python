#!/usr/bin/python
# coding=utf-8
#
# Title:    Subsets
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-10 18:11:27
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        m = self.subsets(nums[:-1])
        return m + [i + [nums[-1]] for i in m]
