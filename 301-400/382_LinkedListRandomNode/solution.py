#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2019-06-24 21:56:42


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.n = 0
        index = self.head
        while index is not None:
            self.n += 1
            index = index.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n = random.randint(0, self.n - 1)
        index = self.head
        for _ in range(n):
            index = index.next
        return index.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
