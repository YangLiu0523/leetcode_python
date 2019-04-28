#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-12-17 08:27:00
"""
Happy Number
"""
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        met_before = set()
        while n != 1:
            n = sum(int(i)*int(i) for i in str(n))
            if n in met_before:
                return False
            met_before.add(n)
        return True
