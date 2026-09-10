# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self,head):
        c=0
        while head!=None:
            c+=1
            head=head.next
        return c
    def reverse(self,head):
        prev=None
        curr=head
        nn=head
        while nn!=None:
            nn=nn.next
            curr.next=prev
            prev=curr
            curr=nn
        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        grps=self.length(head)//k
        ans=None
        prev=None
        while grps>0:
            end=head
            temp=head
            for i in range(1,k):
                end=end.next
            temphead=end.next
            end.next=None
            rh=self.reverse(head)
            if(ans==None):
                ans=rh
            else:
                prev.next=rh
            while temp.next!=None:
                temp=temp.next
            prev=temp
            temp.next=temphead
            head=temphead
            grps-=1
        return ans




        
        