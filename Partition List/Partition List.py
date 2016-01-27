# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(0)
        head2 = ListNode(0)
        index1 = head1
        index2 = head2
        index = head

        while index != None:
            if index.val < x:
                index1.next = ListNode(index.val)
                index1 = index1.next
                index = index.next
            else:
                index2.next = ListNode(index.val)
                index2 = index2.next
                index = index.next
        
        index1.next = head2.next
        return head1.next
