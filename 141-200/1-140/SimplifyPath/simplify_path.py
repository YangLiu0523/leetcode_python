#!/usr/bin/python
# coding=utf-8
#
# Title:    Simplify Path
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-28 23:24:37
#
import os
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        return os.path.abspath(path)        
        
