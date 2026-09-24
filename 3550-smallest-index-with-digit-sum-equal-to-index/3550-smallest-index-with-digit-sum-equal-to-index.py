class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            s=str(nums[i])
            ls=list(s)
            summ=0
            for j in range(len(ls)):
                summ+=int(ls[j])
            if(summ==i):
                return i
        return -1

        