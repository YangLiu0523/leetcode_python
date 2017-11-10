#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 12:16:42
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.flag = True
        self._inorderTraversal(root.left, root.right)
        return self.flag
    
    def _inorderTraversal(self, right, left):
        if right is None or left is None:
            if right != left:
                self.flag = False
            return
        self._inorderTraversal(right.right, left.left)
        if right.val != left.val:
            self.flag = False
        self._inorderTraversal(right.left, left.right)
        
