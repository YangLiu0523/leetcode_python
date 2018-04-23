#!/usr/bin/python
# coding=utf-8
#
# Title:    Remove Suplicates From Sorted List II
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-09-24 22:21:54
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(None)
        end = start
        
        before = ListNode(None)              
        while head:
            if head.val != before.val and (head.next is None or head.next.val != head.val):
                end.next = head
                end = end.next
            before = head
            head = head.next
        
        end.next = None
        return start.next
