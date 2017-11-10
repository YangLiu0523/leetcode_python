#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 15:09:24
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        interval = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:interval+1], inorder[:interval])
        root.right = self.buildTree(preorder[interval+1:], inorder[interval+1:])
        return root
