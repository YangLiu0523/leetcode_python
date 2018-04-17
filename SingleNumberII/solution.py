#!/usr/bin/python
# coding=utf-8
#
# Title: 137. Single Number II
# Author: Lucas
# Date: 2018-04-17 23:04:55
#
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for k, v in counts.items():
            if v == 1:
                return k
