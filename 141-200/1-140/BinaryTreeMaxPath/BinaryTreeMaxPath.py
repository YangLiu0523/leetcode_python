#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-12-12 11:12:02
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        has_root, no_root = self._maxPathSum(root)
        return max(has_root, no_root)

    def _maxPathSum(self, root):
        if root.left:
            l_has_root, l_no_root = self._maxPathSum(root.left)
        if root.right:
            r_has_root, r_no_root = self._maxPathSum(root.right)

        l = [root.val]
        if root.left:
            l[0] += l_no_root
            l.append(l_has_root)
            l.append(l_no_root)
        if root.right:
            l[0] += r_no_root
            l.append(r_has_root)
            l.append(r_no_root)
        has_root = max(l)

        l = [root.val]
        if root.left:
            l.append(l_no_root + root.val)
        if root.right:
            l.append(r_no_root + root.val)
        no_root = max(l)

        return has_root, no_root
