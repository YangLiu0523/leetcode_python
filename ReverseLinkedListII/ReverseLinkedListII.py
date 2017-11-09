#!/usr/bin/env python
# coding=utf-8
# 
# Date: 2017-11-09 11:09:58
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(None)
        h.next = head
               
        start = h
        for _ in range(m - 1):
            start = start.next
        
        end = start.next
        for _ in range(n - m):
            tmp = end.next
            end.next = end.next.next
            tmp.next = start.next
            start.next = tmp
        
        return h.next
