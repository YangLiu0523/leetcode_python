#!/usr/bin/python
# coding=utf-8
#
# Title: 143. Reorder List
# Author: Lucas
# Date: 2018-04-29 11:25:26
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def _length(self, head):
        length = 0
        index = head
        while index:
            length += 1
            index = index.next
        return length

    def _reverse(self, head):
        prev = None
        now = head
        while now:
            next = now.next
            now.next = prev
            prev = now
            now = next

        return prev


    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        if head.next is None:
            return

        length = self._length(head)
        index = head
        for _ in range(length//2-1):
            index = index.next

        first = head
        second = index.next
        index.next = None

        second = self._reverse(second)

        while first:
            first_next = first.next
            second_next = second.next
            first.next = second
            if first_next:
                second.next = first_next
            first = first_next
            second = second_next


def _generate_list(l):
    nodes = [ListNode(val) for val in l]

    for index in range(len(nodes)-1):
        nodes[index].next = nodes[index+1]

    return nodes[0] if nodes else None


def _print_list(head):
    index = head
    l = []
    while index:
        l.append(str(index.val))
        index = index.next

    print(' -> '.join(l))


if __name__ == '__main__':
    h = _generate_list([1, 2, 3, 4])
    Solution().reorderList(h)
    _print_list(h)
