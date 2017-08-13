#!/usr/bin/python
# coding=utf-8
#
# Title:    Title
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-13 16:08:17
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[-1] * n for _ in range(n)]
        circle = 0
        count = 1
        while circle < n/2:
            j = circle
            for i in range(circle, n - circle):
                ret[j][i] = count
                count += 1
            for j in range(circle + 1, n - circle):
                ret[j][i] = count
                count += 1
            for i in range(n - circle - 2, circle - 1, -1):
                ret[j][i] = count
                count += 1
            for j in range(n - circle - 2, circle, -1):
                ret[j][i] = count
                count += 1
            circle += 1
        if n % 2:
            ret[n/2][n/2] = count
        return ret
