#!/usr/bin/python
# coding=utf-8
#
# Title:    Maximum Subarray
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-08 23:28:34
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        m_now = nums[0]
        for i in nums[1:]:
            if m_now > 0:
                m_now += i
            else:
                m_now = i
            if m_now > m:
                m = m_now
        return m
