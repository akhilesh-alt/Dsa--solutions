class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        ans=-1
        for i in range(0,n):
            if(i==0):
                a=nums[0]
            else:
                a=max(nums[0:i])
            b=min(nums[i:n])
            if((a-b)<=k):
                ans=i
                break
        return ans
        
        