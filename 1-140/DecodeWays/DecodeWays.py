#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-11-08 11:17:45
# 
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        n = len(s)
        dp = [0 for _ in xrange(n + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if 1 <= first <= 9:
                dp[i] += dp[i-1]
            if 10 <= second <=26:
                dp[i] += dp[i-2]
        return dp[-1]
