class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n=len(nums)
        ma=0
        for i in range(n):
            ans=0
            for j in range(n):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j])):
                    ans=nums[i]^nums[j]
                    ma=max(ma,ans)
        return ma
        