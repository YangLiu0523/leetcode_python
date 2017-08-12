#!/usr/bin/python
# coding=utf-8
#
# Title:    length of last word
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-12 15:10:57
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        return s[::-1].index(' ') if ' ' in s else len(s)
