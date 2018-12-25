#!/usr/bin/env python
# coding=utf-8
#
# Title: 149. Max points on a line
# Author: Lucas
# Date: 2018-05-22 22:12:33
#
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # Special cases
        if not points:
            return 0
        elif len(points) == 1:
            return 1

        lines = {}
        start = 0
        for start in range(len(points)):
            for end in range(len(points)):
                if start == end:
                    continue
                line = self._get_line(points[start], points[end])
                if line not in lines:
                    lines[line] = set()
                for p, index in [[points[start], start], [points[end], end]]:
                    dim = (p.x, p.y, index)
                    lines[line].add(dim)

        return max([len(v) for v in lines.values()])

    def _get_line(self, point1, point2):
        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y
        if x2 == x1:
            return (x1, None)
        k = (y2-y1) * 10 / (x2-x1)
        b = y1 - k * x1
        return (k, b)
