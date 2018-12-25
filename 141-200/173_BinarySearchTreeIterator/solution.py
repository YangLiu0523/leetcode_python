#!/usr/bin/env python
# coding=utf-8
#
# Title: 173. Binary Search Tree Iterator
# Author: Lucas
# Date: 2018-05-29 21:55:43
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)

    def next(self):
        """
        :rtype: int
        """
        result = self.stack.pop()
        node = result.right
        while node:
            self.stack.append(node)
            node= node.left
        return result.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
