#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-14 23:07:23


import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        nums = set()
        heapq.heappush(heap, 1)
        nums.add(1)
        for i in range(n-1):
            c = heapq.heappop(heap)
            nums.remove(c)
            for p in primes:
                num = p * c
                if num > 4294967296:
                    break
                if num not in nums:
                    heapq.heappush(heap, num)
                    nums.add(num)
        return heapq.heappop(heap)
# TLE
#         nums = set([1])
#         i = 2
#         while len(nums) < n:
#             for p in primes:
#                 if (i / p) in nums:
#                     nums.add(i)
#                     break
#             i += 1
#         # print(nums)

#         return max(nums)
