#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 15:56:09
# 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.result = True
        self._depth(root)
        return self.result
    
    def _depth(self, root):
        l = r = 0
        if root.left:
            l = self._depth(root.left)
        if root.right:
            r = self._depth(root.right)
        if abs(l - r) > 1:
            self.result = False
        return max(l, r) + 1
        
