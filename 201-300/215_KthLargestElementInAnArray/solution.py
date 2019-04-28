# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-14 08:29:21

class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums.sort()
        return nums[-k]
