class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ls=[0]*n
        rs=[0]*n
        ls[0]=0
        rs[n-1]=0
        for i in range(1,n):
            ls[i]=ls[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            rs[i]=rs[i+1]+nums[i+1]
        idx=-1
        for i in range(n):
            if(ls[i]==rs[i]):
                idx=i
                break
        return idx
