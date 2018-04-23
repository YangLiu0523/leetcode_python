#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-09 17:16:06
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.flag = True
        self.max_visited_node = None
        self._inorderTraversal(root)
        return self.flag
    
    def _inorderTraversal(self, node):
        if node.left:
            self._inorderTraversal(node.left)
        self._visit(node)
        if node.right:
            self._inorderTraversal(node.right)
            
    def _visit(self, node):
        print node.val
        if self.max_visited_node is not None and self.max_visited_node >= node.val:
            self.flag = False
        self.max_visited_node = node.val
