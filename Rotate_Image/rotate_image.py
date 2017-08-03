#!/usr/bin/python
# coding=utf-8
#
# Title:    Rotate Image
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-03 21:27:44
#
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix) - 1
        for j in xrange(l):
            for i in xrange(j, l-j):
                matrix[i][j], matrix[l-j][i], matrix[l-i][l-j], matrix[j][l-i] = matrix[l-j][i], matrix[l-i][l-j], matrix[j][l-i], matrix[i][j]
