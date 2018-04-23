#!/usr/bin/python
# coding=utf-8
#
# Title: 139. Word Break
# Author: Lucas
# Date: 2018-04-19 22:03:58
#
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        pool = ['']
        for c in s:
            pool = [elem + c for elem in pool]
            for elem in pool:
                if elem in wordDict:
                    pool.append('')
                    break
        return '' in pool
