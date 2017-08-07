#!/usr/bin/python
# coding=utf-8
#
# Title:    N Queens II
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-07 23:38:16
#
"""
39 ms Fastest Solution
"""
class Solution(object):
    def totalNQueens(self, n):
        cases = [[0, 0, 0]]
        fil = (1 << n) - 1

        for _ in range(n):
            new_cases = []
            for row, ld, rd in cases:
                ld = (ld << 1) & fil
                rd = rd >> 1
                pos = (~(ld | rd | row)) & fil
                while pos:
                    p = pos & (~pos + 1)
                    pos = pos - p
                    new_cases.append([row + p, ld + p, rd + p])
            cases = new_cases

        return len(cases)
