#!/usr/bin/python
# coding=utf-8
#
# Title: 147. Insertion Sort List
# Author: Lucas
# Date: 2018-05-01 09:04:37
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        sorted_head = ListNode(None)
        sorted_head.next = head
        head = head.next
        sorted_head.next.next = None

        while head:
            # pop from origin
            node = head
            head = head.next
            node.next = None

            # add into sorted
            index = sorted_head
            while index.next and index.next.val < node.val:
                index = index.next
            node.next = index.next
            index.next = node

        return sorted_head.next

