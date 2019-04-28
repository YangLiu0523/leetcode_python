# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-01-20 16:51:03
from collections import defaultdict


class Solution:
    def _dfs(self, node):
        if self.orders[node] != -1:
            return True
        if node in self.visited:
            return False

        self.visited.add(node)

        for child in self.requisites[node]:
            if not self._dfs(child):
                return False

        self.orders[node] = self.index
        self.index += 1
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.requisites = defaultdict(list)
        for i, j in prerequisites:
            self.requisites[i].append(j)
        self.orders = [-1] * numCourses

        self.index = 0
        for node in range(numCourses):
            self.visited = set()
            if not self._dfs(node):
                return []

        result = [-1] * numCourses
        for course_id, index in enumerate(self.orders):
            result[index] = course_id
        return result
