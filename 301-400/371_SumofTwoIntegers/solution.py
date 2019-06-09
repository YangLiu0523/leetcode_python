#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-09 20:18:25


class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_filter = 0xffffffff
        while b & bit_filter:
            a, b = a ^ b, (a & b) << 1
            # a, b = a & bit_filter, b & bit_filter
        return a & bit_filter if b > bit_filter else a

