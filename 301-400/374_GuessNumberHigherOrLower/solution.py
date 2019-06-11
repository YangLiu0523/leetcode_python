#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-11 21:10:19


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n

        lo = 1
        hi = n
        while hi > lo:
            mid = (hi + lo) // 2
            tmp = guess(mid)
            if tmp < 0:
                hi = mid
            elif tmp > 0:
                lo = mid
            else:
                return mid
        return hi
