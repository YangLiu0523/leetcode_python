#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-10 15:40:27
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        fast = head
        slow = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if prev is not None:
            prev.next = None
            root.left = self.sortedListToBST(head)
        else:
            root.left = None
        root.right = self.sortedListToBST(slow.next)
        return root
