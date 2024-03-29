#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-11-07 12:12:58
# 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        end_index = m + n - 1
        while index1 >= 0 or index2 >= 0:
            if index1 < 0 or (index2 >= 0 and nums1[index1] < nums2[index2]):
                nums1[end_index] = nums2[index2]
                index2 -= 1
                end_index -= 1
            else:
                nums1[end_index] = nums1[index1]
                index1 -= 1
                end_index -= 1

