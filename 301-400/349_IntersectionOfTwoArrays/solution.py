#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-28 21:17:19


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        for i in nums1:
            if i in nums2:
                ans.append(i)
        return ans
