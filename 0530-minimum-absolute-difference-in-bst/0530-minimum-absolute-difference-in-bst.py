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
        return ls
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ls=[]
        self.ino(root,ls)
        ans=float('inf')
        for i in range(1,len(ls)):
            ans=min(ans,(ls[i]-ls[i-1]))
        return ans
        



        