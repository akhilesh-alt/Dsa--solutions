
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if(head==None):
            return None
        temphead=head
        #zigzag lists
        head=temphead
        while head!=None:
            nn=Node(head.val)
            nn.next=head.next
            head.next=nn
            head=nn.next
        #connecting random pointers of cloned nodes
        head=temphead
        while head!=None:
            if(head.random!=None):
                head.next.random=head.random.next
            head=head.next.next
        #seperate the lists
        head=temphead
        chead=head.next
        ctemp=chead
        while head!=None:
            head.next=head.next.next
            if(head.next!=None):
                ctemp.next=head.next.next
                ctemp=ctemp.next
            head=head.next
        return chead
        

        