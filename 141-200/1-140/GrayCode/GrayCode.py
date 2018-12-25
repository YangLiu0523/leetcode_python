#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-11-07 12:38:55
# 
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in xrange(n):
            result += [2 ** i + j for j in result[::-1]]
        return result
