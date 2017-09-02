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
        if len(word1) == 0 or len(word2) == 0:
            return len(word1 + word2)
        if word1 == word2:
            return 0

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            return 1 + min(
                self.minDistance(word1[1:], word2),
                self.minDistance(word1, word2[1:]),
                self.minDistance(word1[1:], word2[1:])
            )


if __name__ == '__main__':
    word1 = "dinitrophenylhydrazine"
    word2 = "acetylphenylhydrazine"
    print Solution().minDistance(word1, word2)
