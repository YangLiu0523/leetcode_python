#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-23 19:52:49
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def _get(self, index):
        if index not in self.cache:
            self.cache[index] = self.mountain.get(index)
        return self.cache[index]
        
    def findInMountainArray(self, target: int, mountain: 'MountainArray') -> int:
        self.cache = {}
        self.mountain = mountain
        
        # Find mountain top index
        l = mountain.length()
        start = 0
        end = l - 1
        while True:
            if end - start == 1:
                top = start if self._get(start) > self._get(end) else end
                break
            elif end - start == 2:
                mid = (start + end) // 2
                if self._get(mid) > self._get(start) and self._get(mid) > self._get(end):
                    top = mid
                    break
                else:
                    top = start if self._get(start) > self._get(end) else end
                    break
            mid1 = (start + end) // 2
            mid2 = mid1 + 1
            if self._get(mid1) < self._get(mid2):
                start = mid2
            else:
                end = mid1
        
        start = 0
        end = top
        while True:
            if self._get(start) == target:
                return start
            elif self._get(end) == target:
                return end
            mid = (start + end) // 2
            if mid in (start, end):
                break
            if self._get(mid) < target:
                start = mid
            else:
                end = mid
        
        start = top
        end = l - 1
        while True:
            if self._get(start) == target:
                return start
            elif self._get(end) == target:
                return end
            mid = (start + end) // 2
            if mid in (start, end):
                break
            if self._get(mid) > target:
                start = mid
            else:
                end = mid
        return -1
