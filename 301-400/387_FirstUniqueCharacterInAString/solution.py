#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-25 22:18:26


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for c in set(s):
            counts[c] = s.count(c)
        possibles = [c for c in counts.keys() if counts[c] == 1]
        if not possibles:
            return -1
        return min([s.index(c) for c in possibles])
