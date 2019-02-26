#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-26 21:49:30


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        for index, num in enumerate(nums):
            if index == 0:
                result[index] = num
            else:
                result[index] = num * result[index-1]
        tmp = 1
        for index in range(len(nums)-1, -1, -1):
            if index == 0:
                result[index] = tmp
            else:
                result[index] = tmp * result[index-1]
            tmp = tmp * nums[index]
        return result
