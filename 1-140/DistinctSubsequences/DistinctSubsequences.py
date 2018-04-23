#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-15 13:38:50
#
class Solution(object):
    def numDistinct(self, s, t):
        result = [0] * len(t)
        for i in range(len(s)):
            new_result = [0] * len(t)
            for j in range(min(i+1, len(t))):
                new_result[j] = result[j]
                if s[i] == t[j]:
                    new_result[j] += result[j-1] if j > 0 else 1
            result = new_result
        return result[-1]

