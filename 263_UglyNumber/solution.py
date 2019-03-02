#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 10:08:35

class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False

        for u in [2, 3, 5]:
            while num % u == 0:
                num = num // u
        return num == 1
