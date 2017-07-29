#!/usr/bin/python
# coding=utf-8
#
# Title:    Jump Game II
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-07-24 22:38:55
#
class Solution(object):
    def jump(self, nums, count=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while True:
            if len(nums) == 1:
                return count
            if nums[0] == 1:
                nums.pop(0)
                count += 1
                continue
            if nums[0] + 1 >= len(nums):
                nums = nums[-1:]
                count += 1
                continue

            reachable = nums[1:nums[0]+1]
            for i in range(len(reachable)):
                reachable[i] += i
            next_index = reachable.index(max(reachable)) + 1

            if next_index >= len(nums):
                return count + 1
            nums = nums[next_index:]
            count += 1


if __name__ == '__main__':
    test_case = [2, 3, 1, 1, 4]
    # test_case = [1, 2, 3]
    # test_case = [1, 2]
    print Solution().jump(test_case)
