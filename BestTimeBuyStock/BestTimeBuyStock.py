#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-17 17:29:31
# 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        m = prices[0]
        result = 0
        for price in prices:
            if price - m > result:
                result = price - m
            if price < m:
                m = price
        return result
