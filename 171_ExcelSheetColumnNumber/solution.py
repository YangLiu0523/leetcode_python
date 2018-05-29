#!/usr/bin/env python
# coding=utf-8
#
# Title: 
# Author: Lucas
# Date: 2018-05-29 21:54:01
#
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result * 26
            result += ord(c) - ord('A') + 1
        return result
