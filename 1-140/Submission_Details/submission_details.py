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

        ret = []
        last_interval = intervals[0]
        for interval in intervals:
            if interval.start <= last_interval.end:
                last_interval.end = max(interval.end, last_interval.end)
            else:
                ret.append(last_interval)
                last_interval = interval

        ret.append(last_interval)
        return ret
