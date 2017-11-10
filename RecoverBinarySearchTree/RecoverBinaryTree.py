#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 12:00:46
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self._last_visited = None
        self._first = None
        self._second = None
        self._inorderTraversal(root)
        if self._second is None:
            self._second = self._last_visited
        self._first.val, self._second.val = self._second.val, self._first.val
    
    def _inorderTraversal(self, node):
        if node.left:
            self._inorderTraversal(node.left)
        self._visit(node)
        if node.right:
            self._inorderTraversal(node.right)

    def _visit(self, node):
        if (self._last_visited is not None) and (self._first is None) and (self._last_visited.val > node.val):
            self._first = self._last_visited
        if (self._first is not None) and (self._second is None) and (self._first.val < node.val):
            self._second = self._last_visited
        
        self._last_visited = node
