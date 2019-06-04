#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-04 23:54:52


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num:
            i += 1
        # print(i)
        return i * i == num
