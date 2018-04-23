# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeTwoLists(self,l1,l2):
        head=ListNode(250)
        index=head
        index1=l1
        index2=l2
        while index1!=None and index2!=None:
            if index1.val<index2.val:
                index.next=index1
                index1=index1.next
            else:
                index.next=index2
                index2=index2.next
            index=index.next
        if index1==None:
            index.next=index2
        else:
            index.next=index1
        return head.next
        

    def mergeKLists(self, lists):
        begin=None
        if lists==None:
            return None
        for i in lists:
            begin=self.mergeTwoLists(begin,i)
        return begin
