#!/usr/bin/python
# coding=utf-8
#
# Title:    Minimum Window Substring
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-10 17:36:54
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mark = {}
        for i in t:
            if i in mark:
                mark[i] += 1
            else:
                mark[i] = 1
        
        ret = ''
        start = end = 0
        while start < len(s) and end <= len(s):
            #: flag is True if s[start:end] contains T
            flag = True
            for i in mark.values():
                if i > 0:
                    flag = False
        
            if flag and (not ret or len(ret) > len(s[start:end])):
                ret = s[start:end]
            
            if flag:
                if s[start] in mark:
                    mark[s[start]] += 1
                start += 1
            else:
                if end < len(s) and s[end] in mark:
                    mark[s[end]] -= 1
                end += 1
        return ret
