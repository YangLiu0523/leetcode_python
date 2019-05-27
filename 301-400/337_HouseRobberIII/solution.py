#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-27 21:36:38


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _helper(self, node):
        if node is None:
            return 0, 0
        r_with, r_without = self._helper(node.right)
        l_with, l_without = self._helper(node.left)
        return max(node.val + r_without + l_without, r_with + l_with), r_with + l_with

    def rob(self, root: TreeNode) -> int:
        return max(self._helper(root))
