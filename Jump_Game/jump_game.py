#!/usr/bin/python
# coding=utf-8
#
# Title:    Jump Game 85% beat
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-09 23:08:46
#

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distance = 0
        for i in nums[:-1]:
            distance = max(i, distance - 1)
            if distance == 0:
                return False
        return True
