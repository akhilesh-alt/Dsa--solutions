# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def length(self,head):
        c=0
        while head!=None:
            c+=1
            head=head.next
        return c
    def reverse(self,head):
        prev=None
        nxtnode=head
        curr=head
        while nxtnode!=None:
            nxtnode=nxtnode.next
            curr.next=prev
            prev=curr
            curr=nxtnode
        return prev

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if(head==None or head.next==None):
            return head
        k=k%(self.length(head))
        if(k==0):
            return head
        head=self.reverse(head)
        temp=head
        for i in range(1,k):
            temp=temp.next
        shead=temp.next
        temp.next=None
        h1=self.reverse(head)
        h2=self.reverse(shead)
        t1=h1
        while t1.next!=None:
            t1=t1.next
        t1.next=h2
        return h1


        

        