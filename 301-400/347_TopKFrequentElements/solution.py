#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 21:11:08


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        counts = [k_v for k_v in counts.items()]
        counts.sort(key=lambda x: x[1], reverse=True)
        return [counts[i][0] for i in range(k)]
