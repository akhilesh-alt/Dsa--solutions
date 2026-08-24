class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        freq={}
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for k in freq:
            if(freq[k]%2!=0):
                return False
        return True
        