#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 20:53:03


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 1]
        for num in range(2, n+1):
            m = 0
            for left in range(num-1, 0, -1):
                m = max([m, left * ans[num - left], left * (num - left)])
            ans.append(m)
        # print(ans)
        return ans[-1]
