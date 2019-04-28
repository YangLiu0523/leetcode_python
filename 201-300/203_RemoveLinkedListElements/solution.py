#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-12-17 08:34:05
"""
Simple linked list remove action
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pointer = ListNode(-1)
        pointer.next = head

        previous = pointer
        present = head
        while present:
            if present.val == val:
                previous.next = present.next
            else:
                previous = previous.next
            present = present.next
        return pointer.next
