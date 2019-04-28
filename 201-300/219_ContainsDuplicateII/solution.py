# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-19 21:24:29


class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        position = {}
        for index, num in enumerate(nums):
            if num not in position:
                position[num] = []
            position[num].append(index)

        for indexes in position.values():
            for i in range(len(indexes) - 1):
                if indexes[i+1] - indexes[i] <= k:
                    return True

        return False
