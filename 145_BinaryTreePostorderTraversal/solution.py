#!/usr/bin/python
# coding=utf-8
#
# Title: 145. Binary Tree Postorder Traversal
# Author: Lucas
# Date: 2018-04-30 10:47:06
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Preorder and shift right & left
        result = []
        queue = [root] if root else []

        while queue:
            node = queue.pop()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result[::-1]
