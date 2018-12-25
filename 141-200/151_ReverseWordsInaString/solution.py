#!/usr/bin/env python
# coding=utf-8
#
# Title: 151. Reverse words in a string
# Author: Lucas
# Date: 2018-05-23 20:51:06
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([sub_s for sub_s in s.split(' ')[::-1] if sub_s])
