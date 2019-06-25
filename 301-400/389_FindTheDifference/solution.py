#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-25 22:37:09


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in set(t):
            if s.count(c) != t.count(c):
                return c
