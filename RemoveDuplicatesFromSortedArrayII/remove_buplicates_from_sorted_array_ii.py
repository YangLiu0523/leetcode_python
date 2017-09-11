#!/usr/bin/python
# coding=utf-8
#
# Title:    From leetcode
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-11 22:29:18
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t, count = None, 0
        ret = 0

        i = 0
        while i < len(nums):
            if nums[i] == t:
                count += 1
            else:
                t = nums[i]
                count = 1
            if count < 3:
                ret += 1
                i += 1
            else:
                del nums[i]

        return ret
