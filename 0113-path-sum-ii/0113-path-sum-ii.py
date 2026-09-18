# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def paths(self,root,s,ls,ans,targetSum):
        if(root==None):
            return None
        ls.append(root.val)
        s+=root.val
        if(root.left==None and root.right==None):
            if(s==targetSum):
                ans.append(ls[:])
        self.paths(root.left,s,ls,ans,targetSum) 
        self.paths(root.right,s,ls,ans,targetSum)
        ls.pop()

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans=[]
        self.paths(root,0,[],ans,targetSum)
        return ans
        