#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-16 22:41:44
import string


class Solution:
    def _feature(self, word):
        letters = set(word)
        ans = 0
        for c in string.ascii_lowercase:
            ans = ans << 1
            if c in letters:
                ans += 1
        return ans

    def maxProduct(self, words: List[str]) -> int:
        features = []
        for word in words:
            features.append(self._feature(word))

        n = len(words)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if features[i] & features[j] == 0:
                    ans = max(len(words[i]) * len(words[j]), ans)

        return ans
