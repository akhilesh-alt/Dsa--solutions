class Solution(object):
    def solve(self,n,idx,ls,ans,nums):
        if(idx==n):
            ans.append(ls[:])
            return 
        ls.append(nums[idx])
        self.solve(n,idx+1,ls,ans,nums)
        ls.pop()
        self.solve(n,idx+1,ls,ans,nums)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        ans=[]
        self.solve(n,0,[],ans,nums)
        return ans
        