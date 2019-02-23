# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 23:10:13


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Get length
        l = 0
        node = head
        while node:
            l += 1
            node = node.next

        # Split into 2 parts
        right = head
        if l <= 1:
            return True

        if l % 2 == 0:
            mid = head
            for i in range(l // 2 - 1):
                mid = mid.next
            left = mid.next
            mid.next = None
        if l % 2 == 1:
            mid = head
            for i in range(l // 2 - 1):
                mid = mid.next
            left = mid.next.next
            mid.next = None


        right = self._revert(right)

        while left:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True

    def _revert(self, node):
        pres = None
        head = node
        while head:
            # pop(0) from head
            tmp = head
            head = head.next
            tmp.next = pres
            pres = tmp

        return pres
