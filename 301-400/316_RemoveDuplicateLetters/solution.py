#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-16 22:38:39


class Solution:
    def _choose_one(self, letters, ts):
        last_index = {}
        revert = ts[::-1]
        n = len(ts)
        for c in letters:
            last_index[c] = n - revert.index(c) - 1

        last_index = min(last_index.values())
        print(last_index)
        for c in letters:
            if ts.index(c) <= last_index:
                return c
        raise Exception

    def removeDuplicateLetters(self, s: str) -> str:
        letters = set()
        for c in s:
            letters.add(c)
        letters = sorted(letters)

        ans = ''
        ts = s
        while letters:
            c = self._choose_one(letters, ts)
            ans = ans + c
            ts = ts[ts.index(c) + 1:]
            letters.remove(c)
        return ans
