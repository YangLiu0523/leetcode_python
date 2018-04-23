#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-12-12 21:48:48
# 
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        
        m = 0
        for i in nums:
            if i-1 not in numsSet:
                l = 1
                tmp = i
                while tmp+1 in numsSet:
                    tmp += 1
                    l += 1
                if l > m:
                    m = l
        return m
