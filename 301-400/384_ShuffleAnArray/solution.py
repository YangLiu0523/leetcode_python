#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-24 22:24:51


class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.data

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = self.data[:]
        random.shuffle(ans)
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
