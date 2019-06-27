#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-27 21:06:14


class Solution:
    def _right(self, n):
        if n == 1:
            return 1
        if n % 2 == 1:
            return 2 * self._left(n // 2)
        else:
            return 2 * self._left(n // 2) - 1

    def _left(self, n):
        if n == 1:
            return 1
        return 2 * self._right(n // 2)

    def lastRemaining(self, n: int) -> int:
        return self._left(n)
