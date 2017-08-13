#!/usr/bin/python
# coding=utf-8
#
# Title:    Spiral Matrix
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-13 19:16:18
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        row_up = 0
        row_down = len(matrix) - 1
        col_left = 0
        col_right = len(matrix[0]) - 1
        vertical = row_down > col_right
        
        ret = []
        while row_up < row_down and col_left < col_right:
            for i in xrange(col_left, col_right):
                ret.append(matrix[row_up][i])
            for i in xrange(row_up, row_down):
                ret.append(matrix[i][col_right])
            for i in xrange(col_right, col_left, -1):
                ret.append(matrix[row_down][i])
            for i in xrange(row_down, row_up, -1):
                ret.append(matrix[i][col_left])
            row_up += 1
            row_down -= 1
            col_right -= 1
            col_left += 1
        
        if vertical and col_right == col_left:
            for i in xrange(row_up, row_down + 1):
                ret.append(matrix[i][col_right])
        elif not vertical and row_up == row_down:
            for i in xrange(col_left, col_right + 1):
                ret.append(matrix[row_up][i])
        return ret
