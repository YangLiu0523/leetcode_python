#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-24 22:05:01


class Solution:
    def _count(self, s):
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        return count

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = self._count(ransomNote)
        count2 = self._count(magazine)
        for k in count1.keys():
            if count2.get(k, 0) < count1[k]:
                return False
        return True
