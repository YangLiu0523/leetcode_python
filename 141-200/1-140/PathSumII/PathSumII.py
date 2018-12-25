#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 17:08:52
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.result = []
        self.sum = sum
        self.path = []
        self._postorderTraversal(root, 0)
        return self.result
    
    def _postorderTraversal(self, node, total):
        self.path.append(node.val)
        leaf = True
        if node.left:
            self._postorderTraversal(node.left, total + node.val)
            leaf = False
        if node.right:
            self._postorderTraversal(node.right, total + node.val)
            leaf = False
        if leaf and total + node.val == self.sum:
            self.result.append(copy.copy(self.path))
        self.path.pop()
