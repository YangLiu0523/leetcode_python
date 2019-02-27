#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-27 23:31:42


class Solution:
    # O(k*n) Solution
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        for i in range(len(nums)-k+1):
            result.append(max(nums[i:i+k]))
        return result
