#!/usr/bin/python
# coding=utf-8
#
# Title:    Minimum Path Sum
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-26 15:36:29
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = [grid[0][0]]
        for i in range(1, len(grid[0])):
            ret.append(grid[0][i] + ret[i-1])
        
        for i in range(1, len(grid)):
            ret[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                ret[j] = grid[i][j] + min(ret[j], ret[j-1])
        
        return ret[-1]
