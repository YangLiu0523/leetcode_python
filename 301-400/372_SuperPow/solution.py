#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-10 21:57:06


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        a = a % 1337
        b = b[::-1]
        tmp = a % 1337
        for i in range(len(b)):
            base = 1
            for _ in range(b[i]):
                base = (base * tmp) % 1337
            ans = (ans * base) % 1337
            t = 1
            for _ in range(10):
                t = (t * tmp) % 1337
            tmp = t
        return ans % 1337
