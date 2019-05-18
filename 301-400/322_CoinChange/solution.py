#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-18 16:19:20


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        ans = [-1] * (amount + 1)
        ans[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c < 0:
                    break
                if ans[i - c] != -1:
                    if ans[i] == -1 or ans[i] - 1 > ans[i -c]:
                        ans[i] = ans[i-c] + 1
        # print(ans)
        return ans[-1]
