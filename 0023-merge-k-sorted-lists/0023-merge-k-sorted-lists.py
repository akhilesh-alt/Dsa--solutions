# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge(self,h1,h2):
        head=None
        if(h1==None):
            return h2
        if(h2==None):
            return h1
        if(h1.val<h2.val):
            head=h1
            h1=h1.next
        else:
            head=h2
            h2=h2.next
        tail=head
        while h1!=None and h2!=None:
            if(h1.val<h2.val):
                tail.next=h1
                h1=h1.next
            else:
                tail.next=h2
                h2=h2.next
            tail=tail.next
        if h1!=None:
            tail.next=h1
        if h2!=None:
            tail.next=h2
        return head
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        ans=None
        for it in lists:
            ans=self.merge(ans,it)
        return ans
        