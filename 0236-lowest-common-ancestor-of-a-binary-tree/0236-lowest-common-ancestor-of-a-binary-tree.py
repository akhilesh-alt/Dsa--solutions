# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lca(self,root,p,q):
        if(root==None):
            return None
        if(root==p or root==q):
            return root
        l=self.lca(root.left,p,q)
        r=self.lca(root.right,p,q)
        if(l==None and r==None):
            return None
        elif(l!=None and r==None):
            return l
        elif(l==None and r!=None):
            return r
        else:
            return root
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans=0
        ans=self.lca(root,p,q)
        return ans
        