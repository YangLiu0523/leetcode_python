# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 22:44:09


import math


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        s = str(n)
        count = 0
        l = len(str(n))
        for i in range(1, l+1):
            num = int(s[-i])
            count += (n // (10 ** i) + 1) * (10 ** (i-1))
            if num <= 1:
                count -= 10 ** (i-1)
            if num == 1:
                count += n % (10 ** (i-1)) + 1

        return count
