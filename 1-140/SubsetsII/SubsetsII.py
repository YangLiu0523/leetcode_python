#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-11-07 18:29:24
# 
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        while nums:
            i = nums.pop(0)
            length = 1
            while len(nums) > 0 and i == nums[0]:
                length += 1
                nums.pop(0)
            
            combines = [[i] * count for count in range(1, length+1)]
            new = []
            for c in combines:
                new += [j + c for j in result]
            result += new
        return result
