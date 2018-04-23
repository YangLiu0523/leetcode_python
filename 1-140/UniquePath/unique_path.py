#!/usr/bin/python
# coding=utf-8
#
# Title:    Unique Path
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-26 15:08:39
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_grib = []
        for i in range(m):
            dp_grib.append(1)
        
        for _ in range(1, n):
            for j in range(1, m):
                dp_grib[j] += + dp_grib[j-1]
        
        return dp_grib[-1]
