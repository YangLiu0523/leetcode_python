#!/usr/bin/python
# coding=utf-8
#
# Title:    Edit Distance
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-01 22:38:51
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        table = [[-1] * (l2 + 1) for _ in range(l1 + 1)]
        table[0] = range(l2 + 1)
        for i in range(l1 + 1):
            table[i][0] = i

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                case = 0 if word1[i-1] == word2[j-1] else 1
                table[i][j] = min(
                    table[i-1][j] + 1,
                    table[i][j-1] + 1,
                    table[i-1][j-1] + case
                )
        return table[-1][-1]


if __name__ == '__main__':
    word1 = "ab"
    word2 = "bc"
    print Solution().minDistance(word1, word2)
