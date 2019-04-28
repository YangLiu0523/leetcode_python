#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 11:31:14


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        xor = 0
        for i in range(len(nums)+1):
            xor ^= i
        for i in nums:
            xor ^= i
        return xor
