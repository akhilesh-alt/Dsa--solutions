class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=max(nums)
        ans=0
        for i in range(n):
            ans+=(maxi-nums[i])
        return ans
        