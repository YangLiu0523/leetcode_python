#!/usr/bin/python
# coding=utf-8
#
# Title:    Rotate List
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-26 12:04:35
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        index = end = head
        length = 1
        while index.next != None:
            length += 1
            index = index.next
        end = index
        index.next = head

        ret = head
        k = length - (k % length if length != 0 else 0)
        for i in range(k):
            end = ret
            ret = ret.next

        if end is not None:
            end.next = None
        return ret
