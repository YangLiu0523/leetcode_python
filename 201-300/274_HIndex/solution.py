#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-03-02 22:22:25


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for index in range(len(citations)):
            if index + 1 <= citations[index]:
                h = index + 1
            else:
                break
        return h
