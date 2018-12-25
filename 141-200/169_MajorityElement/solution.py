#!/usr/bin/env python
# coding=utf-8
#
# Title: 169. Majority Element
# Author: Lucas
# Date: 2018-05-29 21:53:07
#
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        max_count = 0
        max_num = None
        for n, c in counts.items():
            if c > max_count:
                max_count = c
                max_num = n

        return max_num
