#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-26 08:32:41

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.result = None

        self._post_order(root)
        return self.result

    def _post_order(self, root):
        if root is None:
            return False, False
        if self.result is not None:
            return True, True

        r_p, r_q = self._post_order(root.left)
        l_p, l_q = self._post_order(root.right)

        m_p = self.p is root
        m_q = self.q is root

        p = r_p or l_p or m_p
        q = r_q or l_q or m_q

        if p and q and self.result is None:
            self.result = root
        return p, q
