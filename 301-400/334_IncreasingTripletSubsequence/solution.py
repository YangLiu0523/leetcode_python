#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-26 09:47:34


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second, third = None, None, None
        for num in nums:
            if first is None:
                first = num
            else:
                first = min(num, first)

            if first is not None and num > first:
                if second is None:
                    second = num
                else:
                    second = min(second, num)

            if second is not None and num > second:
                return True

        return False
