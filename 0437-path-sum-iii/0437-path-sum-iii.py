# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def paths(self,root,s,targetSum):
        c=0
        if(root==None):
            return 0
        s+=root.val
        if(s==targetSum):
            c+=1
        c += self.paths(root.left,s,targetSum)
        c += self.paths(root.right,s,targetSum)
        return c
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if(root==None):
            return 0
        return (self.paths(root,0,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum))

        