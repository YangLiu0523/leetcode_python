#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 17:42:55
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        head = TreeNode(None)
        self.now = head
        self._preorderTraversal(root)
    
    def _preorderTraversal(self, root):
        self.now.right = root
        self.now = root
        r = root.right
        l = root.left
        root.left = None
        
        if l:
            self._preorderTraversal(l)
        if r:
            self._preorderTraversal(r)

