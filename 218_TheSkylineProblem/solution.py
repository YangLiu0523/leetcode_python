# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-19 20:57:11


from collections import defaultdict


class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        if not buildings:
            return []
        starts = {}
        ends = {}

        for l, r, h in buildings:
            if l not in starts:
                starts[l] = []
            if r not in ends:
                ends[r] = []
            starts[l].append(h)
            ends[r].append(h)
        points = list(set(list(starts.keys()) + list(ends.keys())))
        points.sort()

        skyline = []
        heights = [0]
        h = 0

        for i in points:
            for r in ends.get(i, []):
                heights.remove(r)
            heights.extend(starts.get(i, []))

            h_new = max(heights)
            if h != h_new:
                skyline.append([i, h_new])
                h = h_new

        return skyline
