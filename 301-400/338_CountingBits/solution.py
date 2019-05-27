#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-27 21:54:29


class Solution:
    def countBits(self, num: int) -> List[int]:
        n = 2
        ans = [0, 1]
        if num < 0:
            return []
        elif num < 2:
            return ans[:num+1]

        for i in range(2, num+1):
            if i == n:
                ans.append(1)
                tmp = 1
                n *= 2
            else:
                ans.append(ans[tmp] + 1)
                tmp += 1
        return ans
