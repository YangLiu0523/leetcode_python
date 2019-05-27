#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-27 08:55:20


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordsdict = {words[i]: i for i in range(len(words))}

        ans = set()
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                tmp1 = word[:j]
                tmp1_reverse = tmp1[::-1]
                tmp2 = word[j:]
                tmp2_reverse = tmp2[::-1]
                if tmp1_reverse in wordsdict and tmp2 == tmp2_reverse:
                    if i != wordsdict[tmp1_reverse]:
                        ans.add((i, wordsdict[tmp1_reverse]))
                if tmp2_reverse in wordsdict and tmp1 == tmp1_reverse:
                    if i != wordsdict[tmp2_reverse]:
                        ans.add((wordsdict[tmp2_reverse], i))
        return list(ans)
