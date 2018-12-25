#!/usr/bin/env python
# coding=utf-8
#
# Title: 166. Fraction to Recurring Decimal
# Author: Lucas
# Date: 2018-05-29 21:48:54
#
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ''
        if numerator * denominator < 0:
            result += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)

        result += str(numerator // denominator)
        maps = {}
        left = numerator % denominator
        if left != 0:
            result += '.'

        while left not in maps and left > 0:
            result += str(left * 10 // denominator)
            maps[left] = len(result) - 1
            left = left * 10 % denominator

        if left != 0:
            split = maps[left]
            result = result[:split] + '(' + result[split:] + ')'
        return result
