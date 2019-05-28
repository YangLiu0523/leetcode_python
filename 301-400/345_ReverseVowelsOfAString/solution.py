#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 21:04:04


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        indexes = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                indexes.append(i)

        i = 0
        j = len(indexes) - 1
        while i < j:
            m, n = indexes[i], indexes[j]
            s[m], s[n] = s[n], s[m]
            i += 1
            j -= 1
        return ''.join(s)

