class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """n=len(nums)
        ans=float('-inf')
        for i in range(n-k+1):
            avg=0
            s=0
            for j in range(i,i+k):
                s+=nums[j]
                avg=float(s)/k
            ans=max(ans,avg)
        return ans"""
        n=len(nums)
        ans=float('-inf')
        s=0
        for i in range(k):
            s+=nums[i]
        avg=float(s)/k
        ans=max(ans,avg)
        for i in range(k,n):
            s-=nums[i-k]
            s+=nums[i]
            avg=float(s)/k
            ans=max(ans,avg)
        return ans

