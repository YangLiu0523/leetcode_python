#!/usr/bin/python
# coding=utf-8
#
# Title:    Set Matrix Zeroes
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-03 17:33:03
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        for row, index_row in zip(matrix, range(len(matrix))):
            for value, index_column in zip(row, range(len(matrix[0]))):
                if value == 0:
                    rows.append(index_row)
                    columns.append(index_column)
        rows = set(rows)
        columns = set(columns)

        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in columns:
            for i in range(len(matrix)):
                matrix[i][j] = 0
