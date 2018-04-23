#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-10-29 16:47:44
# 
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        matrix = [[int(v) for v in row] for row in matrix]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        return max((self.biggestArea(row) for row in matrix))

    def biggestArea(self, row):
        max_area = 0
        for end in xrange(len(row)):
            height = row[end]
            for start in xrange(end, -1, -1):
                if height < row[start]:
                    row[start] = height
                if height > row[start]:
                    height = row[start]
                max_area = max((max_area, height * (end - start + 1)))
        return max_area
