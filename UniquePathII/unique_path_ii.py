#!/usr/bin/python
# coding=utf-8
#
# Title:    Unique Path2
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-26 15:26:55
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        
        ret = [1]
        for j in range(1, len(obstacleGrid[0])):
            ret.append(ret[j - 1] if obstacleGrid[0][j] == 0 else 0)
        
        for i in range(1, len(obstacleGrid)):
            ret[0] = ret[0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    ret[j] = 0
                else:
                    ret[j] += ret[j - 1]
        return ret[-1]
