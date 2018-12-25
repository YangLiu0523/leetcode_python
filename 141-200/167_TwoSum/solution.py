#!/usr/bin/env python
# coding=utf-8
#
# Title: 167. Two Sum
# Author: Lucas
# Date: 2018-05-29 21:50:11
#
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        second = len(numbers) - 1
        while numbers[first] + numbers[second] != target:
            if numbers[first] + numbers[second] > target:
                second -= 1
            else:
                first += 1
        return [first+1, second+1]
