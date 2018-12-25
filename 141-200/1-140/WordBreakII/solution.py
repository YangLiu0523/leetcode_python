#!/usr/bin/python
# coding=utf-8
#
# Title: 140. Word Break
# Author: Lucas
# Date: 2018-04-23 21:21:41
#
# The length of wordDict is much more short than string s
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.map = {}
        return self._dfs(s, wordDict)

    def _dfs(self, s, wordDict):
        if s == '':
            return ['']
        elif s in self.map:
            return self.map[s]

        paths = []
        for word in wordDict:
            if s.startswith(word):
                paths.extend([((word + ' ' + path) if path else word) for path in self._dfs(s.replace(word, '', 1), wordDict)])

        self.map[s] = paths
        return paths
