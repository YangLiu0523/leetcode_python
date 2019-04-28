#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-01 21:57:42

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i

        # Now, xor is a ^ b
        right_different = xor & (-xor)

        a, b = 0, 0
        for i in nums:
            if i & right_different:
                a ^= i
            else:
                b ^= i
        return [a, b]
