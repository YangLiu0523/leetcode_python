#!/usr/bin/python
# coding=utf-8
#
# Title:    Permutation II
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-01 10:09:47
#
class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        return self.permuteSorted(nums)
        
    def permuteSorted(self, nums):
        if len(nums) == 1:
            return [nums]
        ret = []
        old_i = None
        for i in xrange(len(nums)):
            if nums[i] != old_i:
                for j in self.permuteSorted(nums[:i] + nums[i+1:]):
                    ret.append([nums[i]] + j)
                old_i = nums[i]
        return ret
