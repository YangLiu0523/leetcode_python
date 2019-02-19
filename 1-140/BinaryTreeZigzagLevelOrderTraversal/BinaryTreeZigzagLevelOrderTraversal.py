#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 14:53:45
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        reverse = False
        result = []
        level_nodes = [root]
        while level_nodes:
            values = [i.val for i in level_nodes]
            result.append(values[::-1] if reverse else values)
            reverse = not reverse
            
            next_level = []
            for node in level_nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level_nodes = next_level
        return result
