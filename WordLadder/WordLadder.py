#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-12-12 13:41:33
# 
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [beginWord]
        visited = set()
        wordSet = set(wordList)
        level = 1

        while queue:
            level += 1
            new_queue = []
            for w in queue:
                for index in range(len(beginWord)):
                    for c in string.lowercase:
                        temp = w[:index] + c + w[index+1:]

                        if temp in wordSet and temp not in visited:
                            if temp == endWord:
                                return level
                            new_queue.append(temp)
                            visited.add(temp)
            queue = new_queue
        return 0


if __name__ == '__main__':
    b = "hit"
    e = "cog"
    l = ["hot","dot","dog","lot","log"]
    print Solution().ladderLength(b, e, l)
