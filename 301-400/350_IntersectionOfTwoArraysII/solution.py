#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 21:28:43


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count_nums1 = {}
        count_nums2 = {}
        for num in nums1:
            if num not in count_nums1:
                count_nums1[num] = 0
            count_nums1[num] += 1
        for num in nums2:
            if num not in count_nums2:
                count_nums2[num] = 0
            count_nums2[num] += 1

        tmp = {}
        for num in count_nums1.keys():
            if num in count_nums2:
                tmp[num] = min(count_nums1[num], count_nums2[num])

        ans = []
        for k in tmp.keys():
            ans.extend([k] * tmp[k])
        return ans
