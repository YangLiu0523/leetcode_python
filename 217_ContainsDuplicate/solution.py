# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-18 21:49:47


from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        return not (len(set(nums)) == len(nums))
