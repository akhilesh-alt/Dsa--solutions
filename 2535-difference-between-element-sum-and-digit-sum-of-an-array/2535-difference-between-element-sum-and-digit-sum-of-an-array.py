class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        x=0
        y=0
        n=len(nums)
        for i in range(n):
            x+=nums[i]
            num=nums[i]
            while(num!=0):
                y+=num%10
                num=num//10
                
        return abs(x-y)
        