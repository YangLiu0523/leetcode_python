#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-09 19:20:29


class Solution:
    def _dfs(self, index):
        # prefix.append(self.nums[index])
        # if len(prefix) > len(self.ans):
        #     self.ans = prefix[:]
        if index in self.cache:
            return self.cache[index]
        ans = []
        for child in self.path[index]:
            tmp = self._dfs(child)
            if len(tmp) > len(ans):
                ans = tmp[:]
        ans.append(self.nums[index])
        self.cache[index] = ans
        return ans

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        divisers = [[] for i in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    divisers[i].append(j)

        self.cache = {}
        self.nums = nums
        self.path = divisers
        ans = []
        for i in range(len(nums)):
            tmp = self._dfs(i)
            if len(tmp) > len(ans):
                ans = tmp
        # print(self.cache)
        return sorted(ans)
