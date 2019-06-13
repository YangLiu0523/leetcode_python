#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-13 22:30:27


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 2) for _ in range(n+2)]

        for length in range(2, n+1):
            for i in range(1, n + 2 - length):
                # print(i)
                j = i + length - 1
                tmp = j + dp[i][j-1]
                for k in range(i, j+1):
                    tmp = min(tmp, k + max(dp[i][k-1], dp[k+1][j]))
                dp[i][j] = tmp
        # print(dp)
        return dp[1][n]
