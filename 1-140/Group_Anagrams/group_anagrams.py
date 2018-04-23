#!/usr/bin/python
# coding=utf-8
#
# Title:    Group Anagrams
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-03 22:09:51
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        ret_index = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in ret_index:
                ret_index[k] = [s]
                ret.append(ret_index[k])
            else:
                ret_index[k].append(s)
        return ret
        
