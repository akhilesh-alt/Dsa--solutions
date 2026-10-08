def ceil(ans,x):
    l=0
    h=len(ans)-1
    idx=-1
    while l<=h:
        m=(l+h)//2
        if(ans[m]>=x):
            idx=m
            h=m-1
        else:
            l=m+1
    return idx
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        ans=[]
        ans.append(nums[0])
        for i in range(1,n):
            if(nums[i]>ans[len(ans)-1]):
                ans.append(nums[i])
            else:
                cidx=ceil(ans,nums[i])
                ans[cidx]=nums[i]
        return len(ans)
        