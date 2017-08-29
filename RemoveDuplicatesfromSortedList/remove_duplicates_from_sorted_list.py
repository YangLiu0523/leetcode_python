#!/usr/bin/python
# coding=utf-8
#
# Title:    Remove Duplicates From Sorted List
# Author:   Dai Yuanzhen
# Email:    yuanzhendai@gmail.com
# Date:	    2017-08-29 23:39:09
#
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        index = head.next
        previous = head
        while previous.next is not None:
            if index.val == previous.val:
                previous.next = index.next
                index = previous.next
            else:
                previous = previous.next
                index = index.next
        return head
