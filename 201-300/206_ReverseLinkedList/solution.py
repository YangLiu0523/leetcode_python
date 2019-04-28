#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-12-25 21:47:11
"""
206. Reverse Linked List
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "<Node %s>" % self.val

class Solution:
    def add(self, head, node):
        node.next = head
        return node

    def pop(self, head):
        node = head
        head = head.next
        node.next = None
        return node, head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        new_head, left = self.pop(head)
        while left is not None:
            node, left = self.pop(left)
            node.next = new_head
            new_head = node

        return new_head


def main():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next, a2.next, a3.next, a4.next = a2, a3, a4, a5
    result = Solution().reverseList(a1)
    while result:
        print(result)
        result = result.next


if __name__ == '__main__':
    main()
