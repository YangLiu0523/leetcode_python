#!/usr/bin/python
# coding=utf-8
#
# Title:    Combinations
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-10 18:00:53
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [range(1, n+1)]
        
        return self.combine(n-1, k) + [i + [n] for i in self.combine(n-1, k-1)]
