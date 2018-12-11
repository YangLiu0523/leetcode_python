#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-11 08:25:42

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        #
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        if not nums:
            return 0
        max_with_last = nums[0]
        max_without_last = 0

        for i in nums[1:]:
            max_with_last, max_without_last = (
                max(max_without_last + i, max_with_last),
                max_with_last
            )

        return max_with_last
