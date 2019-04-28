#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-24 15:21:11

import copy

class Solution:
    def numSquares(self, n: int) -> int:
        options = [i**2 for i in range(1, int(n ** (1/2)) + 1)]
        visited = {0}
        count = 0
        # print(options)

        while n not in visited:
            new = set()
            for o in options:
                for v in visited:
                    if o + v > n:
                        continue
                    new.add(o+v)
            visited = new
            count += 1

        return count
