#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 15:16:48
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        interval = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:interval], postorder[:interval])
        root.right = self.buildTree(inorder[interval+1:], postorder[interval:-1])
        return root
