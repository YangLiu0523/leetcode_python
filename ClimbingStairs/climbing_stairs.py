#!/usr/bin/python
# coding=utf-8
#
# Title:    Climbing Stairs
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-28 23:20:01
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return b
        
