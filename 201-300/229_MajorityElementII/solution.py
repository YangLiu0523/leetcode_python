# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 16:13:36


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) // 3
        result = []
        for num in set(nums):
            if nums.count(num) > n:
                result.append(num)
        return result
