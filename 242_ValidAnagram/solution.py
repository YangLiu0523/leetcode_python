#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-28 23:41:28

import string


class Solution:
    def _count(self, s):
        result = []
        for c in string.ascii_lowercase:
            result.append(s.count(c))
        return result

    def isAnagram(self, s: str, t: str) -> bool:
        for i, j in zip(self._count(s), self._count(t)):
            if i != j:
                return False
        return True
