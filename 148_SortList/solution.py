#!/usr/bin/python
# coding=utf-8
#
# Title: 148. Sort List
# Author: Lucas
# Date: 2018-05-05 15:36:52
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        h = ListNode(-1)
        h.next = head
        h1 = head

        first = second = h
        while second.next and second.next.next:
            first = first.next
            second = second.next.next

        h2 = first.next
        first.next = None

        first = self.sortList(h1)
        second = self.sortList(h2)

        # Merge
        index = h
        while first or second:
            if not first:
                node = second
                second = second.next
            elif not second:
                node = first
                first = first.next
            elif first.val < second.val:
                node = first
                first = first.next
            else:
                node = second
                second = second.next
            node.next = None

            index.next = node
            index = index.next

        return h.next
