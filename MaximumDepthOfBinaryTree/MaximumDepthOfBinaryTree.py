#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 14:57:46
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.depth = 0
        self._inorderTraversal(root, 1)
        return self.depth
    
    def _inorderTraversal(self, node, level):
        if node.left:
            self._inorderTraversal(node.left, level + 1)
        if level > self.depth:
            self.depth = level
        if node.right:
            self._inorderTraversal(node.right, level + 1)
