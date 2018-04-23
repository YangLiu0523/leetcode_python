#!/usr/bin/python
# coding=utf-8
#
# Title: 142. Linked List Cycle II
# Author: Lucas
# Date: 2018-04-23 22:21:23
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                count = 1
                fast = fast.next
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None
