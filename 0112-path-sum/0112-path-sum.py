# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root,s,targetSum):
        if(root==None):
            return False
        s+=root.val
        if(root.left==None and root.right==None):
            return s==targetSum
        return self.check(root.left,s,targetSum) or self.check(root.right,s,targetSum)
        
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        return self.check(root,0,targetSum)

        