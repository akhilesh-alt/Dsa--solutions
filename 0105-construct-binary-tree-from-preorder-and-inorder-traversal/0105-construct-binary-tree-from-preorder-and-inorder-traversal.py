# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def create(self,preorder,inorder,n,l,h):
        global hm,idx
        if(l>h):
            return None
        root=TreeNode(preorder[idx])
        pos=hm[preorder[idx]]
        idx+=1
        root.left=self.create(preorder,inorder,n,l,pos-1)
        root.right=self.create(preorder,inorder,n,pos+1,h)
        return root
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        global hm,idx
        idx=0
        hm={}
        n=len(preorder)
        for i in range(n):
            hm[inorder[i]]=i
    
        root=self.create(preorder,inorder,n,0,n-1)
        return root
        

        