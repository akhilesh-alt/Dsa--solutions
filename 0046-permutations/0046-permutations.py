class Solution(object):
    def solve(self,n,nums,idx,ls,vis,ans):
        if(idx==n):
            ans.append(ls[:])
            return
        for i in range(n):
            if(vis[i]==True):
                ls.append(nums[i])
                vis[i]=False
                self.solve(n,nums,idx+1,ls,vis,ans)
                vis[i]=True
                ls.pop()
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        vis=[True]*(n)
        ans=[]
        self.solve(n,nums,0,[],vis,ans)
        return ans
        