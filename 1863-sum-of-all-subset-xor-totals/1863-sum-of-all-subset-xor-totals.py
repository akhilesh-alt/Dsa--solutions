class Solution(object):
    def solve(self,n,idx,nums,ls):
        ans=0
        if(idx==n):
            c=0
            for i in range(len(ls)):
                c^=ls[i]
            return c
        ls.append(nums[idx])
        ans+=self.solve(n,idx+1,nums,ls)
        ls.pop()
        ans+=self.solve(n,idx+1,nums,ls)
        return ans


            
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        return self.solve(n,0,nums,[])

        