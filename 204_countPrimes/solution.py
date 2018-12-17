#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-12-17 08:58:08
"""
Count Primes
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime = [True] * n

        for i in range(2, n):
            if not prime[i]:
                continue
            for j in range(2, (n-1) // i + 1):
                prime[i * j] = False
        return prime.count(True) - 2
