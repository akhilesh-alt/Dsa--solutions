class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        """ans=float('inf')
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if(s>=target):
                    ans=min(ans,(j-i+1))
                    break
        if(ans==float('inf')):
            return 0
        return ans"""

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


        