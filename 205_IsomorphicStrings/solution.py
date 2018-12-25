#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-25 21:25:57
"""
205. Isomorphic Strings
"""
import string


class Solution:
    def _key(self, s):
        char_map = {}
        for c in s:
            if c not in char_map:
                char_map[c] = string.printable[len(char_map)]

        return ''.join([char_map[c] for c in s])

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self._key(s) == self._key(t)


if __name__ == '__main__':
    from sample import cases
    for args, result in cases:
        print("Running with case:", args, result)
        assert Solution().isIsomorphic(*args) == result
