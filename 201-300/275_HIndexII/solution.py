#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 23:18:47


class Solution:
    def _fit(self, citations, index):
        return citations[index] >= len(citations) - index

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        start = 0
        end = len(citations) - 1
        if self._fit(citations, start):
            return len(citations)
        if not self._fit(citations, end):
            return 0

        while end - start > 1:
            mid = (start + end) // 2
            if self._fit(citations, mid):
                end = mid
            else:
                start = mid
        return len(citations) - end
