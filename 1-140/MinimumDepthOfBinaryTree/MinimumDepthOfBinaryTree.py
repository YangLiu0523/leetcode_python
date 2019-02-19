#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 16:43:44
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if r == 0:
            return l + 1
        if l == 0:
            return r + 1
        return min(r, l) + 1
