#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-17 17:24:35
# 
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
            triangle[i][-1] += triangle[i-1][-1]
        return min(triangle[-1])
