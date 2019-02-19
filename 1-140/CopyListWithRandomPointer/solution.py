#!/usr/bin/python
# coding=utf-8
#
# Title: 138. Copy List with Random Pointer
# Author: Lucas
# Date: 2018-04-19 21:37:34
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Ensure at least 1 node
        if head is None:
            return None

        pres = head
        # 1 -> 2 -> 3 to 1 -> 1' -> 2 -> 2' -> 3 -> 3'
        while pres:
            next = pres.next
            pres.next = RandomListNode(pres.label)
            pres.next.next = next
            pres = next

        # Add random link to new nodes
        old_pres = head
        while old_pres:
            new_pres = old_pres.next
            new_pres.random = old_pres.random.next if old_pres.random else None
            old_pres = new_pres.next

        # Restore old and new
        old_pres = head
        new_head = head.next
        while True:
            new_pres = old_pres.next
            old_pres.next = new_pres.next
            old_pres = old_pres.next
            if old_pres:
                new_pres.next = old_pres.next
            else:
                break

        return new_head
