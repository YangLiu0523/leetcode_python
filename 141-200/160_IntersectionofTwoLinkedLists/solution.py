#!/usr/bin/env python
# coding=utf-8
#
# Title: 160. Intersection of Two Linked Lists
# Author: Lucas
# Date: 2018-05-29 21:32:30
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        index1 = headA
        len1 = 1
        while index1.next:
            len1 += 1
            index1 = index1.next
        index2 = headB
        len2 = 1
        while index2.next:
            len2 += 1
            index2 = index2.next
        if index1 != index2:
            return None

        while len1 > len2:
            headA = headA.next
            len1 -= 1
        while len2 > len1:
            headB = headB.next
            len2 -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

