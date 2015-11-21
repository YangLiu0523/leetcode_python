# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return head
        
        temp=head.next
        head.next=head.next.next
        temp.next=head
        head=temp
        index=head.next
        
        while index.next != None:
            if index.next.next == None:
                break
            temp=index.next.next
            index.next.next=temp.next
            temp.next=index.next
            index.next=temp
            index=temp.next
            
        return head
        
