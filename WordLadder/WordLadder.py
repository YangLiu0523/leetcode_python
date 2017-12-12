#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-12-12 13:41:33
# 
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = {w:[] for w in wordList}
        wordDict[beginWord] = []
        for i1 in range(len(wordList)-1):
            for i2 in range(i1+1, len(wordList)):
                if self._similar(wordList[i1], wordList[i2]):
                    wordDict[wordList[i1]].append(wordList[i2])
                    wordDict[wordList[i2]].append(wordList[i1])
        for i2 in range(len(wordList)):
            if self._similar(wordList[i2], beginWord):
                wordDict[beginWord].append(wordList[i2])

        prev = [beginWord]
        result = {}
        step = 1
        while prev:
            new_prev = []
            for w in prev:
                if w == endWord:
                    return step
                for w_next in wordDict[w]:
                    if w_next not in result:
                        result[w_next] = step + 1
                        new_prev.append(w_next)
            prev = new_prev
            step += 1

        return 0


    def _similar(self, s1, s2):
        if len(s1) != len(s2):
            return False
        flag = False
        for i in xrange(len(s1)):
            if s1[i] == s2[i]:
                continue
            if not flag:
                flag = True
            else:
                return False
        return True


