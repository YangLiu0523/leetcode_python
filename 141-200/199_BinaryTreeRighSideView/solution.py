#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-12-11 08:42:37

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        if len(right) > len(left):
            return [root.val] + right
        else:
            return [root.val] + right + left[len(right):]
