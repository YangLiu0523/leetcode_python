#!/usr/bin/python
# coding=utf-8
#
# Title:    Permutation II
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-01 10:09:47
#
class Solution(object):
    def permute(self, nums):
        result = [[]]
        for i in nums:
            new_result = []
            for perm in result:
                for j in xrange(len(perm) + 1):
                    new_result.append(perm[:j] + [i] + perm[j:])
            result = new_result
        return result
