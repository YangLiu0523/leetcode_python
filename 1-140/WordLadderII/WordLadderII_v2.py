#!/usr/bin/env python
# coding=utf-8
#
# Question: 126. Word Ladder II
# Date: 2018-04-10 21:02:51
#
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
        unreached = set(copy.deepcopy(wordList))
        shortest_path = {beginWord: [[beginWord]]}
        while shortest_path:
            new_shortest_path = {}
            for s1, paths in shortest_path.items():
                for s2 in self._less_than_one(s1, unreached):
                    new_paths = [path + [s2] for path in paths]
                    if s2 in new_shortest_path:
                        new_shortest_path[s2].extend(new_paths)
                    else:
                        new_shortest_path[s2] = new_paths

            for s2, paths in new_shortest_path.items():
                unreached.remove(s2)
                if s2 == endWord:
                    return paths
            shortest_path = new_shortest_path

        return []

    def _less_than_one(self, s1, unreached):
        # count = 0
        # for index in range(len(s1)):
            # if s1[index] != s2[index]:
                # count += 1
            # if count > 1:
                # return False
        # return True
        result = []
        for index in range(len(s1)):
            for c in string.ascii_lowercase:
                word = s1[:index] + c + s1[index+1:]
                if word in unreached and word not in result:
                    result.append(word)
        return result

if __name__ == '__main__':
    b = "nanny"
    e = "aloud"
    import json
    with open('large_case.json', 'r') as fp:
        l = json.load(fp)
    print(Solution().findLadders(b, e, l))
