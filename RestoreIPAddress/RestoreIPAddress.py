#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-09 11:43:12
# 
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dp = [['', s]]
        for i in range(4, 0, -1):
            new_dp = []
            for prefix, left in dp:
                l = len(left)
                if l > 3 * i or l < i:
                    break
                min_l = max(1, l - i * 3 + 3)
                max_l = 1 if left.startswith('0') else min(3, l - i + 1)
                for b in range(min_l, max_l+1):
                    if 0 <= int(left[:b]) <= 255:
                        new_dp.append([prefix+left[:b]+'.', left[b:]])
            dp = new_dp
        return [i[0][:-1] for i in dp]
                
