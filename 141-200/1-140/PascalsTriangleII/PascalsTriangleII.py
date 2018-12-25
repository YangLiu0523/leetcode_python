#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-17 17:19:27
# 
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(rowIndex):
            result = [i+j for i, j in zip([0]+result, result+[0])]
        return result
