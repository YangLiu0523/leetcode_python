#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-23 19:51:49


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        for i in range(256):
            if count[i] != 0:
                min_v = i
                break

        for i in range(256):
            if count[i] != 0:
                max_v = i

        sum_v = 0
        total = 0
        for i in range(256):
            sum_v += i * count[i]
            total += count[i]
        mean_v = sum_v / total

        used = 0
        for i in range(256):
            used += count[i]
            if used == total // 2:
                median_v = i
                for j in range(i+1, 256):
                    if count[j] != 0:
                        median_v += j
                        break
                median_v = median_v / 2
                break
            elif used > total // 2:
                median_v = i
                break

        max_c = max(count)
        mode_v = count.index(max_c)

        return float(min_v), float(max_v), float(mean_v), float(median_v), float(mode_v)
