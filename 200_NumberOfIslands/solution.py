#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-15 15:25:27
"""
Leetcode 200. Number of Islands
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    lands.add((i, j))

        land_count = 0
        while lands:
            queue = [lands.pop()]
            while queue:
                i, j = queue.pop()
                for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if neighbor in lands:
                        lands.remove(neighbor)
                        queue.append(neighbor)
            land_count += 1
        return land_count
