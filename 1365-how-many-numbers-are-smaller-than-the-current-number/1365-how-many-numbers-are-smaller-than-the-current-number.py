class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n=len(nums)
        arr=sorted(nums)
        d={}
        for i in range(n):
            if(arr[i] not in d):
                d[arr[i]]=i
        ans=[]
        for num in nums:
            ans.append(d[num])
        return ans


        