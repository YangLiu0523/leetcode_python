#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-09 20:54:51
"""
189. Rotate Array

Easy
"""

class Solution:
    def rotate(self, nums, k):
        l = len(nums)
        k = k % len(nums)
        self.revert(nums, 0, l-k-1)
        self.revert(nums, l-k, l-1)
        self.revert(nums, 0, l-1)


    def revert(self, nums, start, end):
        i = 0
        while start + i < end - i:
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]
            i += 1

def main():
    cases = (
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([-1, -100, 3, 99], 2)
    )
    for nums, k in cases:
        Solution().rotate(nums, k)
        print(nums)


if __name__ == '__main__':
    main()
