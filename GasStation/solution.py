#!/usr/bin/python
# coding=utf-8
#
# Title: 134. Gas Station
# Author: Lucas
# Date: 2018-04-15 22:54:49
#
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0:
            return -1
        elif len(gas) == 1:
            return 0 if (gas[0] >= cost[0]) else -1

        # start = 0
        s = 0
        min_s = gas[0] - cost[0]
        min_s_index = 0
        for end in range(0, len(gas)):
            s += (gas[end] - cost[end])
            if s < min_s:
                min_s = s
                min_s_index = end

        return (min_s_index+1) % len(gas) if (sum(gas) - sum(cost) >= 0) else -1
