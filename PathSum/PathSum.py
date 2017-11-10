#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 17:01:41
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        self.result = False
        self.sum = sum
        self._postorderTraversal(root, 0)
        return self.result

    def _postorderTraversal(self, node, above):
        leaf = True
        if node.left:
            self._postorderTraversal(node.left, above+node.val)
            leaf = False
        if node.right:
            self._postorderTraversal(node.right, above+node.val)
            leaf = False
        if leaf and above + node.val == self.sum:
            self.result = True
