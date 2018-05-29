#!/usr/bin/env python
# coding=utf-8
#
# Title: 165. Compare Version Numbers
# Author: Lucas
# Date: 2018-05-29 21:46:37
#
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        while version1 and version2:
            if version1[0] > version2[0]:
                return 1
            elif version1[0] < version2[0]:
                return -1
            version1.pop(0)
            version2.pop(0)

        if version1:
            for i in version1:
                if i > 0:
                    return 1
        if version2:
            for i in version2:
                if i > 0:
                    return -1
        return 0
