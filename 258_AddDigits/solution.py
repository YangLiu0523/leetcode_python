#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-28 23:51:11

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        digits = []
        while num != 0:
            digits.append(num % 10)
            num = num // 10
        return self.addDigits(sum(digits))
