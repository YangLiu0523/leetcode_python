#!/usr/bin/env python
# coding=utf-8
#
# Title:
# Author: Lucas
# Date: 2018-05-24 19:44:00
#
import copy
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        imax = imin = r = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(nums[i], imax*nums[i])
            imin = min(nums[i], imin*nums[i])

            r = max(r, imax)

        return r


if __name__ == '__main__':
    case = [2, 3, -2, 4]
    print(Solution().maxProduct(case))
