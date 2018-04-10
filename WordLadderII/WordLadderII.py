#!/usr/bin/python
# coding=utf-8
#
# Date: 2017-12-13 22:34:23
#
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import string
import copy


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        wordDict = {w: [] for w in wordList}
        for w in wordList:
            for index in range(len(w)):
                for c in string.ascii_lowercase:
                    temp = w[:index] + c + w[index+1:]
                    if temp in wordDict:
                        wordDict[w].append(temp)

        # BFS
        unvisited = set(wordList)
        unvisited.remove(beginWord)
        queue = [
            [[beginWord], unvisited]
        ]
        flag = False
        while queue:
            new_queue = []
            for sequence, unvisited in queue:
                for nextWord in wordDict[sequence[-1]]:
                    if nextWord not in unvisited:
                        continue
                    elif nextWord == endWord:
                        flag = True
                    unvisited = copy.deepcopy(unvisited)
                    unvisited.remove(nextWord)
                    new_queue.append([sequence + [nextWord], unvisited])
            queue = new_queue
            if flag:
                break
        if flag:
            result = []
            for s, _ in queue:
                if s[-1] == endWord:
                    result.append(s)
            return result
        return []


if __name__ == '__main__':
    b = "cet"
    e = "ism"
    import json
    with open('large_case.json', 'r') as fp:
        l = json.load(fp)
    print(Solution().findLadders(b, e, l))
