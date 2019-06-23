#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-23 20:13:13


import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        value_index = {}
        heap = []
        for i in range(n):
            v = matrix[i][0]
            if v not in value_index:
                value_index[v] = []
            value_index[v].append((i, 0))
            heapq.heappush(heap, v)

        for _ in range(k - 1):
            v = heapq.heappop(heap)
            i, j = value_index[v].pop()
            if j + 1 < n:
                nv = matrix[i][j+1]
                heapq.heappush(heap, nv)
                if nv not in value_index:
                    value_index[nv] = []
                value_index[nv].append((i, j+1))
        return heapq.heappop(heap)
