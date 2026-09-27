class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=float('inf')
        p1=0
        p2=0
        s=0
        while p2<n:
            s+=nums[p2]
            while s>=target:
                ans=min(ans,(p2-p1+1))
                s-=nums[p1]
                p1+=1
            p2+=1
        if(ans==float('inf')):
            return 0
        return ans
        