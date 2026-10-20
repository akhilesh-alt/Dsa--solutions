class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if(nums[j]-nums[i]==diff and nums[k]-nums[j]==diff):
                        c+=1
        return c


        