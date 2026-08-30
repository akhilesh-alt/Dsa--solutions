class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        maxi=float('-inf')
        mini=float('inf')
        maxidx=-1
        minidx=-1
        for i in range(n):
            if(nums[i]>maxi):
                maxi=nums[i]
                maxidx=i
            if(nums[i]<mini):
                mini=nums[i]
                minidx=i
        left=-1
        right=-1
        left=min(minidx,maxidx)
        right=max(minidx,maxidx)
        a1=(right+1)
        a2=(n-left)
        a3=(left+1)+(n-right)
        return min(a1,a2,a3)


        
        

        