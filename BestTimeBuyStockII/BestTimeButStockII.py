#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-12-03 15:53:58
# 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        deltas = [j - i for i, j in zip(prices[:-1], prices[1:])]
        result = 0
        for i in deltas:
            if i > 0:
                result += i
        return result
