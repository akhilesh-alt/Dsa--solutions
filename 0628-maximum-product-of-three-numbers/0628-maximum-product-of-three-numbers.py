class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=float('-inf')
        nums.sort()
        a1=nums[n-1]*nums[n-2]*nums[n-3]
        a2=nums[0]*nums[1]*nums[n-1]
        return max(a1,a2)

        
        