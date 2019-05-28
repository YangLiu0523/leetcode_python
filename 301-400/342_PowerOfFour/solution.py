#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 20:30:43


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num != 1:
            if num % 4 == 0:
                num = num // 4
            else:
                return False
        return True
