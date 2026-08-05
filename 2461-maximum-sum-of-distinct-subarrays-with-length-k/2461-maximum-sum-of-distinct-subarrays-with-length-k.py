class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp={}
        n=len(nums)
        ans=0
        s=0
        for i in range(0,k):
            mp[nums[i]]=mp.get(nums[i],0)+1
            s+=nums[i]
        if(len(mp)==k):
            ans=s
        for i in range(k,n):
            mp[nums[i-k]]=mp.get(nums[i-k],0)-1
            s-=nums[i-k]
            if(mp[nums[i-k]]==0):
                del mp[nums[i-k]]
            s+=nums[i]
            mp[nums[i]]=mp.get(nums[i],0)+1
            if(len(mp)==k):
                ans=max(ans,s)
        return ans




        