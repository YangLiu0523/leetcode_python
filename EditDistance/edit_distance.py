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
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(
                        table[i-1][j],
                        table[i][j-1],
                        table[i-1][j-1]
                    )
        return table[-1][-1]


if __name__ == '__main__':
    word1 = "dinitrophenylhydrazinedinitrophenylhydrazinedinitrophenylhydrazinedinitrophenylhydrazine"
    word2 = "acetylphenylhydrazineacetylphenylhydrazineacetylphenylhydrazineacetylphenylhydrazine"
    print Solution().minDistance(word1, word2)
