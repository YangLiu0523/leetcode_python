#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-30 22:02:18


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Edge cases
        if len(envelopes) <= 1:
            return len(envelopes)

        # Sort the envelopes so that env[0] is increasing and env[1] is decreasing
        # Put env[1] into seq
        m = max([env[1] for env in envelopes]) + 1
        envelopes.sort(key=lambda x: x[0] - x[1] / m)
        seq = [env[1] for env in envelopes]
        # print(envelopes, seq)

        # Find the longest increasing subsequence of seq
        ans = [seq[0]]
        for num in seq[1:]:
            if num > ans[-1]:
                ans.append(num)
                continue
            if num <= ans[0]:
                ans[0] = num
                continue
            # Binary search
            i = 0
            j = len(ans) - 1
            while j - i > 1:
                mid = (j + i) // 2
                if ans[mid] < num:
                    i = mid
                else:
                    j = mid
            ans[j] = num
            # print(ans, num)
        # print(ans)
        return len(ans)
