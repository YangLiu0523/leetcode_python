#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-18 15:27:22


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []
        possibilities = set([(0, 0)])
        left = k
        n1 = len(nums1)
        n2 = len(nums2)
        while left:
            # print(left, possibilities)
            tmp = set()
            m = -1
            for s1, s2 in possibilities:
                l1 = n1 - s1
                l2 = n2 - s2
                m2 = max(0, left - l1) - 1
                m1 = max(0, left - l2) - 1
                pop_value = max(nums1[s1:n1-m1] + nums2[s2:n2-m2])
                if pop_value < m:
                    continue
                elif pop_value > m:
                    tmp = set()
                    m = pop_value
                if pop_value in nums1[s1:n1-m1]:
                    tmp.add((nums1.index(pop_value, s1)+1, s2))
                if pop_value in nums2[s2:n2-m2]:
                    tmp.add((s1, nums2.index(pop_value, s2)+1))
            possibilities = tmp
            ans.append(m)
            left -= 1
        return ans

