# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        Len=1
        index_node=head
        while not index_node.next==None:
            Len+=1
            index_node=index_node.next
        need=Len-n
        index_node=head
        if need==0:
            return head.next
        index=1
        while index<need:
            index+=1
            index_node=index_node.next
        index_node.next=(index_node.next).next
        return head
