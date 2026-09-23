# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxpath(self,root):
        if(root==None):
            return 0
        l=self.maxpath(root.left)
        r=self.maxpath(root.right)
        if(l<0):
            l=0
        if(r<0):
            r=0
        self.ans=max(self.ans,(l+root.val+r))
        return max(l+root.val,r+root.val)
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans=float('-inf')
        self.maxpath(root)
        return self.ans
        