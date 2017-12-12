#!/usr/bin/python
# coding=utf-8
# 
# Date: 2017-12-12 22:00:43
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        l = self._postOrder(root)
        return sum([int(s) for s in l])

    def _postOrder(self, node):
        result = []
        if node.left:
            result = result + self._postOrder(node.left)
        if node.right:
            result = result + self._postOrder(node.right)

        c = str(node.val)
        if not result:
            return [c]
        else:
            return [c + i for i in result]
