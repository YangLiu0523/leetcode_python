# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 16:22:32


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.k = k
        self.result = None

        self._inorder_traversal(root)

        return self.result

    def _inorder_traversal(self, root):
        if root is None:
            return
        if self.count >= self.k:
            return

        self._inorder_traversal(root.left)

        # Visit this node
        self.count += 1
        if self.count == self.k:
            self.result = root.val

        self._inorder_traversal(root.right)
