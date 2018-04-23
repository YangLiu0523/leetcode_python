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
        rows = set()
        columns = set()
        for index_row in range(len(matrix)):
            for index_column in range(len(matrix[0])):
                if matrix[index_row][index_column] == 0:
                    rows.add(index_row)
                    columns.add(index_column)

        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in columns:
            for i in range(len(matrix)):
                matrix[i][j] = 0
