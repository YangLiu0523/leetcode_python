#!/usr/bin/python
# coding=utf-8
#
# Title:    Permutation Sequence
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-20 21:21:57
#
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k - 1
        ret = ''
        left = [str(i) for i in range(1, n+1)]
        modes = [] if n == 1 else [1]
        for i in range(2, n):
            modes.append(modes[-1] * i)
        for mode in modes[::-1]:
            index = k / mode
            ret += left[index]
            k = k - index * mode
            left = left[:index] + left[index + 1:]
        ret += left[0]
        return ret
        
