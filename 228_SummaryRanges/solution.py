# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 16:09:55

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = end = nums.pop(0)
        nums.append([-1])

        result = []
        for num in nums:
            if start is None:
                start = end = num
            elif num == end + 1:
                end = num
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append("%d->%d" % (start, end))
                start = end = num

        return result
