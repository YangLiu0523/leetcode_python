#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-25 21:25:57
"""
207. Course Schedule

Slow solution, faster than 5.54%
"""


class Solution:
    def _do_task(self, job_id):
        self.tasks_left.remove(job_id)
        for task_id in self.dependencies:
            if job_id in self.dependencies[task_id]:
                self.dependencies[task_id].remove(job_id)

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.tasks_left = set(list(range(numCourses)))
        self.dependencies = {task_id: [] for task_id in range(numCourses)}
        for task, dep in prerequisites:
            self.dependencies[task].append(dep)

        while True:
            left_count = len(self.tasks_left)

            for task_id in list(self.tasks_left):
                if not self.dependencies[task_id]:
                    self._do_task(task_id)
            if len(self.tasks_left) == 0:
                return True
            elif len(self.tasks_left) == left_count:
                return False


if __name__ == '__main__':
    from sample import cases
    for args, result in cases:
        print("Running with case:", args, result)
        assert Solution().canFinish(*args) == result
