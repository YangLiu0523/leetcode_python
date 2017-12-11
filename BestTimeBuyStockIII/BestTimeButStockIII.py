#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-12-11 22:25:57
# 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # trade1
        trade1 = []
        min_before = prices[0]
        max_delta = 0
        for p in prices:
            max_delta = max(max_delta, p - min_before)
            min_before = min(p, min_before)
            trade1.append(max_delta)

        # trade2
        trade2 = []
        max_after = prices[-1]
        max_delta = 0
        for p in prices[::-1]:
            max_delta = max(max_delta, max_after - p)
            max_after = max(p, max_after)
            trade2.append(max_delta)
        trade2 = trade2[::-1]

        return max([i + j for i, j in zip([0] + trade1, trade2 + [0])])


if __name__ == '__main__':
    prices = [7, 4, 5, 1, 3, 2, 6, 3]
    print Solution().maxProfit(prices)
