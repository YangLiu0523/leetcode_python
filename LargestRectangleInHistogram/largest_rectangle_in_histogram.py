#!/usr/bin/python
# coding=utf-8
#
# Title:    Largest Rectangle in Histogram
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-10-01 20:06:44
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = len(heights)
        lessFromLeft = [-1] * l
        lessFromRight = [l] * l
        
        for i in range(1, l):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p
        
        for i in range(l - 2, -1, -1):
            p = i + 1
            while p < l and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p
        
        max_area = 0
        for i in range(l):
            area = heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1)
            if area > max_area:
                max_area = area
        return max_area

