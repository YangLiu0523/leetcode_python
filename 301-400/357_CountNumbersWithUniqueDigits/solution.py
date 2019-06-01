#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-01 15:18:11


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Generate A(l, 10) and A(l, 9)
        a_9 = [1]
        a_10 = [1]
        for i in range(9, 0, -1):
            a_9.append(a_9[-1] * i)
        for i in range(10, 0, -1):
            a_10.append(a_10[-1] * i)

        # print(a_9, a_10)

        count = 0
        for l in range(min(n+1, 11)):
            if l == 0:
                count += 1
            else:
                count += a_10[l] - a_9[l-1]
        return count
