#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-09 14:08:57
# 
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return False
        
        if s1[-1] == s2[-1] == s3[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1]) or self.isInterleave(s1, s2[:-1], s3[:-1])
        elif s1[-1] == s3[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1])
        elif s2[-1] == s3[-1]:
            return self.isInterleave(s1, s2[:-1], s3[:-1])
        else:
            return False
