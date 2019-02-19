#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-17 17:16:48
# 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            result.append([i+j for i, j in zip(result[-1]+[0], [0]+result[-1])])
        return result
