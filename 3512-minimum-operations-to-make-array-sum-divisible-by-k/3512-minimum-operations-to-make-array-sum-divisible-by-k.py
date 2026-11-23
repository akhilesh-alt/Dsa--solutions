class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=0
        for i in range(len(nums)):
            s+=nums[i]
        return s%k
        