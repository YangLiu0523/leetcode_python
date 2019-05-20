#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-20 23:19:00
"""
O((m*n) * lg(m*n)) solution
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = [[1] * n for _ in range(m)]
        # print(ans)

        indexes = []
        for i in range(m):
            for j in range(n):
                indexes.append((i, j, matrix[i][j]))
        indexes.sort(key=lambda x: x[2])

        for i, j, v in indexes:
            for k, l in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if k < 0 or l < 0 or k >= m or l >= n:
                    continue
                if matrix[k][l] < v:
                    ans[i][j] = max(ans[i][j], ans[k][l] + 1)
        # print(ans)
        return max([max(row) for row in ans])
