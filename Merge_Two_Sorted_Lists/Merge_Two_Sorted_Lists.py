#!/usr/bin/python
#Filename:Merge_Two_Sorted_List.py

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
class Solution:
    def mergeTwoLists(self,l1,l2):
        index1=l1
        index2=l2
        head=ListNode(666)
        index3=head
        if index1==None:
            return l2
        elif index2==None:
            return l1
        while index1 and index2:
            if index1.val<index2.val:
                Next=ListNode(index1.val)
                index3.next=Next
                index1=index1.next
            else:
                Next=ListNode(index2.val)
                index3.next=Next
                index2=index2.next
            index3=index3.next
        if not index1:
            index3.next=index2
        else:
            index3.next=index1
        return head.next

