#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-28 23:47:41


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.path = []
        self.result = []
        self._dfs(root)
        return self.result

    def _dfs(self, node):
        if node is None:
            return
        self.path.append(str(node.val))

        if not (node.left or node.right):
            self.result.append('->'.join(self.path))
        else:
            self._dfs(node.left)
            self._dfs(node.right)

        self.path.pop()
