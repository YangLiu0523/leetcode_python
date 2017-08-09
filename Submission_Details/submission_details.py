#!/usr/bin/python
# coding=utf-8
#
# Title:    submission details
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-09 23:33:06
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        
        def start_value(interval):
            return interval.start
        
        intervals.sort(key=start_value)
        
        ret = [intervals.pop(0)]
        while intervals != []:
            now = intervals.pop(0)
            if now.start <= ret[-1].end:
                ret[-1].end = max(now.end, ret[-1].end)
            else:
                ret.append(now)
        return ret
