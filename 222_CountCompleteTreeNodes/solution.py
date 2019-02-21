# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-21 21:58:51

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: 'TreeNode') -> 'int':
        self.count = 0
        self._traversal(root)
        return self.count

    def _traversal(self, node):
        if node is None:
            return
        self.count += 1

        self._traversal(node.left)
        self._traversal(node.right)
