#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-20 21:47:12
"""
This solution is from discuss. So I will first implement it and then try to
implement my own solution.
"""


class Solution:
    def __init__(self):
        self.aux = None
        self.upper = None
        self.lower = None

    def _mergesort(self, nums, lo, hi):
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        count = self._mergesort(nums, lo, mid) + self._mergesort(nums, mid, hi)

        # Count range sum for i in [lo:mid] and j in [mid:hi]
        i = j = mid
        for left in nums[lo:mid]:
            while i < hi and nums[i] - left < self.lower:
                i += 1
            while j < hi and nums[j] - left <= self.upper:
                j += 1
            count += j - i

        # Merge nums[lo:mid] and nums[mid:hi]
        i = lo
        j = mid
        for index in range(lo, hi):
            if i == mid:
                self.aux[index] = nums[j]
                j += 1
            elif j == hi:
                self.aux[index] = nums[i]
                i += 1
            elif nums[i] <= nums[j]:
                self.aux[index] = nums[i]
                i += 1
            else:
                self.aux[index] = nums[j]
                j += 1
        for index in range(lo, hi):
            nums[index] = self.aux[index]
        return count

    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        self.aux = [0] * (n + 1)
        self.lower = lower
        self.upper = upper
        sum_to_i = [0] * (n + 1)
        print(sum_to_i)
        for i, v in enumerate(nums):
            sum_to_i[i+1] = sum_to_i[i] + nums[i]
        return self._mergesort(sum_to_i, 0, n + 1)


def main():
    testcases = [
        ((-2, 5, -1), -2, 2, 3)
    ]
    for nums, lower, upper, target in testcases:
        ans = Solution().countRangeSum(nums, lower, upper)
        assert ans == target, "%d != %d" % (ans, target)


if __name__ == '__main__':
    main()
