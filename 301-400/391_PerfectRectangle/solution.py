#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-27 22:09:25


class Solution:
    def _test_line(self, line):
        # line.sort(key=lambda x: x[0])
        for i in range(len(line) - 1):
            if line[i][1] != line[i+1][0]:
                return False

        if line[0][0] != self.start:
            return False
        if line[-1][1] != self.end:
            return False
        return True

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        lines = {}
        rectangles.sort(key=lambda x:x[1])
        m = None
        for x1, y1, x2, y2 in rectangles:
            for i in range(x1, x2):
                if i not in lines:
                    if m is None:
                        m = y1
                    elif m != y1:
                        return False
                elif lines[i] != y1:
                    return False
                lines[i] = y2

        for i in range(min(lines.keys()), max(lines.keys()) + 1):
            if i not in lines:
                return False
        max_y = lines.values()
        return min(max_y) == max(max_y)
