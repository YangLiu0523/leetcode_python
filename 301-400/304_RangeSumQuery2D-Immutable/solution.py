#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-02 21:09:57


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for row in matrix:
            s = [0]
            for n in row:
                s.append(s[-1] + n)
            self.sums.append(s)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i, j = col1, col2
        s = 0
        for row in range(row1, row2+1):
            s += self.sums[row][j+1] - self.sums[row][i]

        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
