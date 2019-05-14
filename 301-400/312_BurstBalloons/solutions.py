#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-14 22:26:34


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for l in range(3, n+1):
            for left in range(0, n - l + 1):
                right = left + l - 1

                # for i in range(left + 1, right):
                #     dp[left][right] = max(
                #         dp[left][right],
                #         nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                #     )
                dp[left][right] = max([
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right)
                ])
        return dp[0][n-1]
