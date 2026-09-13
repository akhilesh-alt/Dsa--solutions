class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """n=len(nums)
        c=0
        if k<=1:
            return 0
        for i in range(n):
            p=1
            for j in range(i,n):
                p*=nums[j]
                if(p<k):
                    c+=1
        return c"""
        n=len(nums)
        l=0
        r=0
        p=1
        c=0
        if k<=1:
            return 0
        while r<n:
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            c+=(r-l+1)
            r+=1
        return c


        