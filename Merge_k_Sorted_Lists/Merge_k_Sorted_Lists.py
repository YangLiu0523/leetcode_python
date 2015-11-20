class Solution(object):
    def mergeKLists(self, lists):
        if lists == None:
            return None
        numbers=[]    
        for i in lists:
            while i!=None:
                numbers.append(i.val)
                i=i.next
        numbers.sort()
        head=ListNode(2)
        index=head
        for i in numbers:
            index.next=ListNode(i)
            index=index.next
        return head.next
