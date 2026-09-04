class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """n=len(nums)
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
        return ans"""
        n=len(nums)
        maxi=[0]*n
        maxi[0]=nums[0]
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i-1])
        mini=[0]*n
        mini[0]=min(nums)
        for i in range(1,n):
            mini[i]=min(nums[i:n])
        ans=-1
        for i in range(n):
            a=maxi[i]
            b=mini[i]
            if((a-b)<=k):
                ans=i
                break
        return ans


        
        