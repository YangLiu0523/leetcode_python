#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-09 16:52:33
"""
Any solution with *i* days could be separated into 2 kinds,

  1. Last day is the end of the last transaction
  2. Last day is not in any transaction

*j*: Max transactions number
*global*
*local*

diff = prices[i] - prices[i-1]
local[i][j]  = max(local[i-1][j]+diff, global[i-1][j-1] + diff)
global[i][j] = max(local[i][j], global[i-1][j])
"""

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        if k >= len(prices) / 2:
            return sum(
                b - a
                for a, b in zip(prices[:-1], prices[1:])
                if b > a
            )

        local_max = [0] * (k + 1)
        global_max = [0] * (k + 1)

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]

            for j in range(k, 0, -1):
                local_max[j] = max(local_max[j], global_max[j-1]) + diff
                global_max[j] = max(local_max[j], global_max[j])

        return global_max[k]


def main():
    cases = (
        (2, [3, 2, 6, 5, 0, 3]),
        (2, [1, 3, 2, 6, 5, 0, 3]),
    )
    for args in cases:
        print(Solution().maxProfit(*args))


if __name__ == '__main__':
    main()
