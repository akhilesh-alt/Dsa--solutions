from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if(root==None):
            return None
        q=deque()
        q.append(root)
        while(len(q)>0):
            f=q.popleft()
            f.left,f.right=f.right,f.left
            if(f.left!=None):
                q.append(f.left)
            if(f.right!=None):
                q.append(f.right)
    
        return root
        


        