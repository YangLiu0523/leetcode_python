#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-09 14:01:41
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self._dfs(1, n+1)
    
    def _dfs(self, start, end):
        if start == end:
            return [None]
        elif end - start == 1:
            return [TreeNode(start)]
        result = []
        
        for interval in range(start, end):
            left_trees = self._dfs(start, interval)
            right_trees = self._dfs(interval+1, end)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(interval)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result
