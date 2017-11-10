#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 12:09:29
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None or q is None:
            return p == q
        self.equal = True
        self._inorderTraversal(p, q)
        return self.equal
        
    def _inorderTraversal(self, node1, node2):
        if node1.left:
            if not node2.left:
                self.equal = False
            else:
                self._inorderTraversal(node1.left, node2.left)
        elif node2.left:
                self.equal = False
        if node1.val != node2.val:
            self.equal = False
        if node1.right:
            if not node2.right:
                self.equal = False
            else:
                self._inorderTraversal(node1.right, node2.right)
        elif node2.right:
            self.equal = False
