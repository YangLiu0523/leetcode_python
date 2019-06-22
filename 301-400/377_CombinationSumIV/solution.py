#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-22 21:32:13


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        l = len(nums)
        nums.sort()
        ans = [0] * (target + 1)
        ans[0] = 1

        for total in range(1, target + 1):
            for num in nums:
                diff = total - num
                if diff < 0:
                    break
                ans[total] += ans[diff]
        return ans[-1]
