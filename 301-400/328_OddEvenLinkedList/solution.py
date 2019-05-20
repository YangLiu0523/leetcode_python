#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-05-20 22:59:55


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        first = ListNode(None)
        f_i = first
        second = ListNode(None)
        s_i = second

        index = head
        count = 0
        while index:
            if count % 2 == 0:
                f_i.next = index
                f_i = index
            elif count % 2 == 1:
                s_i.next = index
                s_i = index
            index = index.next
            count += 1
        f_i.next = second.next
        s_i.next = None
        return first.next
