#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-04 22:48:57


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if y < x:
            x, y = y, x
        possibles = set()
        tmp = {0, x, y}
        while tmp:
            new_tmp = set()
            for v in tmp:
                if v < 0 or v in possibles:
                    continue
                if z in [v, v + x, min(v, x) + y]:
                    return True
                possibles.add(v)
                new_tmp.add(abs(v - x))
                new_tmp.add(abs(v - y))
            tmp = new_tmp
        return False
