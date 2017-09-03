#!/usr/bin/python
# coding=utf-8
#
# Title:    Search a 2D Matrix
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-03 17:46:42
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        len_y = len(matrix)
        if len_y == 0:
            return False
        len_x = len(matrix[0])
        return target in [matrix[i / len_x][i % len_x] for i in range(len_x * len_y)]
