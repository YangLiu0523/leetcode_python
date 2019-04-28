# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-21 21:46:20

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: 'int', t: 'int') -> 'bool':
        if t < 0:
            return False

        cache = {}
        for index, num in enumerate(nums):
            if index - k > 0:
                bucket_id_remove = nums[index - k - 1] // (t + 1)
                del cache[bucket_id_remove]

            bucket_id = num // (t + 1)

            if bucket_id in cache:
                return True
            if bucket_id - 1 in cache and abs(cache[bucket_id-1] - num) <= t:
                return True
            if bucket_id + 1 in cache and abs(cache[bucket_id+1] - num) <= t:
                return True

            cache[bucket_id] = nums[index]
        return False
