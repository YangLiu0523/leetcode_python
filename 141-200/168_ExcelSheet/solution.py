#!/usr/bin/env python
# coding=utf-8
#
# Title: 168. Excel Sheet
# Author: Lucas
# Date: 2018-05-29 21:51:27
#
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n:
            result = chr(ord('A') + (n-1) % 26) + result
            n = (n-1) // 26
        return result
