#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-02-26 08:23:48

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p, self.q = p, q
        self.result = None
        self._post_order(root)
        return self.result

    def _post_order(self, root):
        if root is None:
            return False, False

        l_p, l_q = self._post_order(root.left)
        r_p, r_q = self._post_order(root.right)

        m_p, m_q = False, False
        if root is self.p:
            m_p = True
        if root is self.q:
            m_q = True

        p = l_p or r_p or m_p
        q = l_q or r_q or m_q
        if p and q and self.result is None:
            self.result = root

        return p, q
