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
        if(p.val>root.val and q.val>root.val):
            return self.lca(root.right,p,q)
        elif(p.val<root.val and q.val<root.val):
            return self.lca(root.left,p,q)
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
        
        