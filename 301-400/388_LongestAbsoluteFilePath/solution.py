#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-25 22:34:59


class Solution:
    def lengthLongestPath(self, s: str) -> int:
        lines = s.split('\n')
        depths = [l.count('\t') for l in lines]
        lengths = [0] * (max(depths) + 1)
        # path = [''] * len(lengths)

        ans = 0
        for i in range(len(lines)):
            line = lines[i]
            depth = depths[i]
            line = line.replace('\t', '')
            if '.' not in line:
                # path[depth] = line
                depths[depth] = (depths[depth-1] if depth > 0 else 0) + len(line) + 1
            else:
                ans = max(
                    ans,
                    (depths[depth - 1] if depth > 0 else 0) + len(line)
                )
                # print(path, line)
        return ans
