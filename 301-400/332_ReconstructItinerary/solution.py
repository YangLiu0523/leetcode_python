#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-22 23:00:28
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets, key=lambda x: (x[0] + x[1]), reverse=True):
            targets[a].append(b)  #  += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

