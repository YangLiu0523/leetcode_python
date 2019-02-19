#!/usr/bin/python
# coding=utf-8
#
# Title: 132. Palindrome Partitioning II
# Author: Lucas
# Date: 2018-04-12 21:36:05
#
"""
"aab" can be divided by 1 cut to ["aa", "b"]
.....................

"abaac"
"aba", "a", "c"
or
"a", "b", "aa", "c"

possibles = ["aba", "aa", "c"]
a b a a c
_ _ _ _ _
_____
    ___

Maybe using DP?

"""
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # TODO: is_palindrome can be create in O(n^2)
        is_palindrome = [[False] * len(s) for _ in range(len(s))]
        for start in range(len(s)):
            for end in range(start, len(s)):
                is_palindrome[start][end] = (s[start:end+1] == (s[start:end+1])[::-1])

        min_cuts = [0] * len(s)
        for start in range(len(s)-1, -1, -1):
            if is_palindrome[start][-1]:
                min_cuts[start] = 0
                continue
            temp = []
            for split in range(start, len(s)-1):
                if is_palindrome[start][split]:
                    temp.append(min_cuts[split+1])
            min_cuts[start] = min(temp) + 1
        return min_cuts[0]
