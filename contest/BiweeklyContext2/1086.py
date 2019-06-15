#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-15 22:33:48


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores = {}
        for student, score in items:
            if student not in scores:
                scores[student] = []
            scores[student].append(score)
        ans = []
        for student in scores.keys():
            ans.append([student, sum(sorted(scores[student])[-5:]) // 5])

        ans.sort(key=lambda x: x[0])
        return ans



