#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 21:59:25


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        for i, interval in enumerate(self.intervals):
            if interval[0] <= val <= interval[1]:
                return
            if val == interval[0] - 1:
                interval[0] = val
                if i > 0 and self.intervals[i-1][1] == val - 1:
                    self.intervals[i-1][1] = interval[1]
                    self.intervals.pop(i)
                return
            elif val == interval[1] + 1:
                interval[1] = val
                if i < (len(self.intervals) - 1) and self.intervals[i+1][0] == val + 1:
                    self.intervals[i+1][0] = interval[0]
                    self.intervals.pop(i)
                return

        index = 0
        while index < len(self.intervals):
            if self.intervals[index][0] > val:
                break
            index += 1
        self.intervals = self.intervals[:index] + [[val, val]] + self.intervals[index:]

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        # print(self.intervals)
        return self.intervals



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
