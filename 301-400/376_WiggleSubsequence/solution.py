#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-20 23:36:39
"""
1    1 :1     1 :1
17   17:2     1 :1
5    17:2     5 :3
10   10:4     10:3
13   13:4     10:4
15   15:5     15:4
10   15:5     10:6
5    15:5     5 :6
16   16:7     5 :6
8    16:7     8 :8
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        new = []
        for n in nums:
            if not new or n != new[-1]:
                new.append(n)
        nums = new
        if len(nums) <= 1:
            return len(nums)

        up = nums[1] > nums[0]
        last = nums[1]
        length = 2
        for v in nums[2:]:
            if up:
                if v > last:
                    last = v
                elif v < last:
                    length += 1
                    up = False
                    last = v
            elif not up:
                if v < last:
                    last = v
                elif v > last:
                    length += 1
                    up = True
                    last = v
        return length


def main():
    testcases = [
        ([1,7,4,9,2,5], 6),
        ([1,17,5,10,13,15,10,5,16,8], 7),
        ([1,2,3,4,5,6,7,8,9], 2)
    ]
    for case, target in testcases:
        ans = Solution().wiggleMaxLength(case)
        assert ans == target, "%s %s!=%s" % (case, ans, target)


if __name__ == '__main__':
    main()
