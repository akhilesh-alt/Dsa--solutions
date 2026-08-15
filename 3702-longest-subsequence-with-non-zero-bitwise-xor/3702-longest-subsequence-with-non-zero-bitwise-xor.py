class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(n):
            ans^=nums[i]
        if(ans!=0):
            return n
        for x in nums:
            if(x!=0):
                return n-1
        return 0
        