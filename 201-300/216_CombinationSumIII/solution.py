# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-18 21:47:31

class Solution:
    def combinationSum3(self, k: 'int', n: 'int', start=1) -> 'List[List[int]]':
        if k == 1:
            if 1 <= n <= 9:
                return [[n]]
            return []
        if n < (1 + k) * k / 2 or n > (9 - k + 1 + 9) * k / 2:
            return []

        result = set()
        for i in range(start, 10):
            for sub_result in self.combinationSum3(k-1, n-i, i+1):
                if i not in sub_result:
                    result.add(tuple(sorted(sub_result + [i])))
        return [
            list(sorted(i)) for i in result
        ]
