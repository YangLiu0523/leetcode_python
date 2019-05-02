#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-02 21:03:08


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = [0]
        for n in nums:
            self.sum.append(self.sum[-1] + n)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1] - self.sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
