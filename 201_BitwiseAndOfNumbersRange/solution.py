#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-12-15 17:52:26

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
            n &= n-1
        return n


