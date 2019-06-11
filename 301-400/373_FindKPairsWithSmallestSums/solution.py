#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-11 21:00:09


import heapq


class Solution:
    @staticmethod
    def _add_to_combine(combine, pair, value):
        if value not in combine:
            combine[value] = []
        combine[value].append(pair)

    @staticmethod
    def _remove_from_combine(combine, value):
        pair = combine[value].pop()
        if not combine[value]:
            combine.pop(value)
        return pair

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1:
            return []

        combine = {}    # Key is the sum and Value is a list of possibles to sum to it
        heap = []
        for j in range(len(nums2)):
            heapq.heappush(heap, nums1[0] + nums2[j])
            self._add_to_combine(combine, (0, j), nums1[0] + nums2[j])

        ans = []
        for _ in range(k):
            # print(heap, combine)
            if not combine:
                break
            value = heapq.heappop(heap)
            i, j = self._remove_from_combine(combine, value)
            ans.append([nums1[i], nums2[j]])

            i += 1
            if i < len(nums1):
                heapq.heappush(heap, nums1[i] + nums2[j])
                self._add_to_combine(combine, (i, j), nums1[i] + nums2[j])

        return ans
