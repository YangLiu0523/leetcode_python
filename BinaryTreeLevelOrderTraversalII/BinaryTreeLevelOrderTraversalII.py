#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 15:23:24
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.result = []
        self._preorderTraversal(root, 0)
        return self.result[::-1]

    def _preorderTraversal(self, node, level):
        if len(self.result) <= level:
            self.result.append([node.val])
        else:
            self.result[level].append(node.val)
        if node.left:
            self._preorderTraversal(node.left, level+1)
        if node.right:
            self._preorderTraversal(node.right, level+1)
