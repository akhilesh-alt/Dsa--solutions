# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def create(self,inorder,postorder,l,h):
        if(l>h):
            return None
        root=TreeNode(postorder[self.idx])
        pos=self.hm[postorder[self.idx]]
        self.idx-=1
        root.right=self.create(inorder,postorder,pos+1,h)
        root.left=self.create(inorder,postorder,l,pos-1)
        return root
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.hm={}
        n=len(inorder)
        for i in range(n):
            self.hm[inorder[i]]=i
        self.idx=n-1
        root=self.create(inorder,postorder,0,n-1)
        return root
        


        