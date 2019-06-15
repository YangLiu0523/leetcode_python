#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-15 22:30:53


class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = min(A)
        ans = sum([int(c) for c in str(m)])
        return 0 if ans % 2 == 1 else 1
