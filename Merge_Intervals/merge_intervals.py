#!/usr/bin/python
# coding=utf-8
#
# Title:    Merge Intervals
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-11 00:05:42
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        flag = len(intervals)
        for i in range(len(intervals)):
            if intervals[i].start > newInterval.start:
                flag = i
                break
        intervals = intervals[:flag] + [newInterval] + intervals[flag:]
        ret = []

        if flag > 1:
            ret = intervals[:flag-1]
            intervals = intervals[flag-1:]
        
        last_interval = intervals[0]
        for interval in intervals:
            if interval.start <= last_interval.end:
                last_interval.end = max(interval.end, last_interval.end)
            else:
                ret.append(last_interval)
                last_interval = interval
        
        ret.append(last_interval)
        return ret
