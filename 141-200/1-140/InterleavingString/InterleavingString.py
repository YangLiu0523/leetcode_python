#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-09 14:09:27
# 
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        
        index = [[0, 0]]
        for c in s3:
            new_index = []
            for i, j in index:
                if i < l1 and s1[i] == c and [i+1, j] not in new_index:
                    new_index.append([i+1, j])
                if j < l2 and s2[j] == c and [i, j+1] not in new_index:
                    new_index.append([i, j+1])
            index = new_index
        return bool(index)
