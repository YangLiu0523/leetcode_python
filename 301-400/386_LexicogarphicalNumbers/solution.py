#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-25 22:11:35


class Solution:
    def _dfs(self, ans, current, n):
        ans.append(n)
        for i in range(10):
            next_value = 10 * current + i
            if next_value >= n:
                break
            self._dfs(ans, next_value, n)

    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        if n <= 1:
            return ans

        self._dfs(ans, 1, n)
        return ans
