class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=float('-inf')
        for i in range(n):
            for j in range(i+1,n):
                p=((nums[i]-1)*(nums[j]-1))
                ans=max(ans,p)
        return ans
        