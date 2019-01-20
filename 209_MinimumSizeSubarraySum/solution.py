#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-25 21:25:57
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = end = 0

        nums_sum = 0
        result = len(nums) + 1
        while True:
            if nums_sum < s:
                if end >= len(nums):
                    break
                nums_sum += nums[end]
                end += 1
            else:
                nums_sum -= nums[start]
                start += 1

            if nums_sum >= s:
                result = min(end - start, result)
        if result == len(nums) + 1:
            return 0
        return result


if __name__ == '__main__':
    from sample import cases
    for args, result in cases:
        print("Running with case:", args, result)
        act_result = Solution().minSubArrayLen(*args)
        print("Result is %s" % act_result)
        assert act_result == result
