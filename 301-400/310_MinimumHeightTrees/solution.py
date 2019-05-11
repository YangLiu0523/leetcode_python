#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-11 15:59:27


"""
How many MHTs can a graph have at most?
ans: 2?
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]

        link = [set() for _ in range(n)]
        for i, j in edges:
            link[i].add(j)
            link[j].add(i)

        degree = [len(link[i]) for i in range(n)]
        removed = [i for i in range(n) if degree[i] == 1]

        while True:
            new = []

            for p in removed:
                degree[p] = 0
                for child in link[p]:
                    if degree[child]:
                        degree[child] -= 1
                        if degree[child] == 1:
                            new.append(child)
            if not new:
                return removed

            removed = new
