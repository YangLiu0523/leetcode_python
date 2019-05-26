#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-26 15:46:37


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        for i in range(3, len(x)):
            a, b, c, d = x[i-3:i+1]
            if c <= a and d >= b:
                # print(1)
                return True

        for i in range(4, len(x)):
            a, b, c, d, e = x[i-4:i+1]
            if a + e == c and b == d:
                # print(2)
                return True

        for i in range(5, len(x)):
            a, b, c, d, e, f = x[i-5:i+1]
            if c > a and d >= b and e <= c and a + e >= c and b + f >= d:
                # print(3, a, b, c, d, e, f)
                return True
        return False
