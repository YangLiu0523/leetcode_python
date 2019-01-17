#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-25 21:25:57
"""
207. Course Schedule

The problem equals to judge whether the graph have loop.
"""

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        taken_course = [False] * numCourses

        def dfs(course):
            """Whether the graph has loop dfs from point *course*"""
            if taken_course[course]:
                return True

            if course in visited:
                return False
            else:
                visited.add(course)

            for req in graph[course]:
                if taken_course[req]:
                    continue
                if not dfs(req):
                    return False

            taken_course[course] = True
            return True

        for course in range(numCourses):
            visited = set()
            if not dfs(course):
                return False

        return True


if __name__ == '__main__':
    from sample import cases
    for args, result in cases:
        print("Running with case:", args, result)
        assert Solution().canFinish(*args) == result
