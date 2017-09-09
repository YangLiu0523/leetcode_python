#!/usr/bin/python
# coding=utf-8
#
# Title:    Sort Colors
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-09 17:50:31
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        i1 = 0
        for i in xrange(len(nums)):
            tmp = nums[i]
            nums[i] = 2
            if tmp <= 1:
                nums[i1] = 1
                i1 += 1
            if tmp == 0:
                nums[i0] = 0
                i0 += 1
        
