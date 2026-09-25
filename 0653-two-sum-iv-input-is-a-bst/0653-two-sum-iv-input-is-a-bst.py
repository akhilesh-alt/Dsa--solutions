# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def ino(self,root,ls):
        if(root==None):
            return None
        self.ino(root.left,ls)
        ls.append(root.val)
        self.ino(root.right,ls)

    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        ls=[]
        self.ino(root,ls)
        p1=0
        p2=len(ls)-1
        while p1<p2:
            if(ls[p1]+ls[p2]==k):
                return True
            elif(ls[p1]+ls[p2]>k):
                p2-=1
            else:
                p1+=1
        return False
        