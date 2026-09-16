# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self,nums,l,h):
        if l>h:
            return None
        m=(l+h)//2
        root=TreeNode(nums[m])
        root.left=self.insert(nums,l,m-1)
        root.right=self.insert(nums,m+1,h)
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.insert(nums,0,len(nums)-1)
        