# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-13 21:10:30
class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if len(nums) == 1:
            return nums[0]

        return max(
            self._rob1_helper(nums[:-1]),
            self._rob1_helper(nums[1:])
        )

    def _rob1_helper(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        s_0 = nums[0]
        s_1 = max(nums[1], nums[0])

        for num in nums[2:]:
            s_0, s_1 = s_1, max(s_1, s_0 + num)

        return max(s_0, s_1)
