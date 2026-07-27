class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=0
        nums.sort()
        for i in range(0,n,2):
            mini=min(nums[i],nums[i+1])
            s+=mini
        return s


        