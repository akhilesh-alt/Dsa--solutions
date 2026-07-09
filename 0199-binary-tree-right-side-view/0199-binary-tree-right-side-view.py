from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        if(root==None):
            return res
        q=deque()
        q.append(root)
        while(len(q)>0):
            s=len(q)
            for i in range(s):
                f=q.popleft()
                if(i==s-1):
                    res.append(f.val)
                if(f.left!=None):
                    q.append(f.left)
                if(f.right!=None):
                    q.append(f.right)
            
        return res

        
        