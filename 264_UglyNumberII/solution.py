#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 11:24:29

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [1]
        indexes = [0, 0, 0]
        while len(result) < n:
            nextes = [result[i] * j for i, j in zip(indexes, [2, 3, 5])]
            next_num = min(nextes)
            for i in range(3):
                if nextes[i] == next_num:
                    indexes[i] += 1
            result.append(next_num)
        return result[-1]
