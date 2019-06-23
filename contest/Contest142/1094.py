#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-23 19:52:05


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass_diff = [0] * 1001

        for user, start, end in trips:
            pass_diff[start] += user
            pass_diff[end] -= user

        count = 0
        for i in range(1001):
            count += pass_diff[i]
            if count < 0 or count > capacity:
                return False
        return True
