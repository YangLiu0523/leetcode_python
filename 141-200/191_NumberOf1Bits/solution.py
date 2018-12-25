#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-12-11 08:06:22

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
