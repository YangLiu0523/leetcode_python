#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 23:55:07


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        if isBadVersion(start):
            return start

        while end - start > 1:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        return end
