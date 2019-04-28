#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-28 08:54:08


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        i = len(matrix) - 1
        j = 0
        j_m = len(matrix[0])

        while i >= 0 and j < j_m:
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                j += 1
            else:
                i -= 1
        return False
