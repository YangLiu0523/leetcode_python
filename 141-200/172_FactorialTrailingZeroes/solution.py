#!/usr/bin/env python
# coding=utf-8
#
# Title: 172. Factorial Trailing Zeroes
# Author: Lucas
# Date: 2018-05-29 21:54:55
#
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n // 5
            n = n // 5
        return result
