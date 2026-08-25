class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set()
        n=len(nums)
        for i in range(n):
            s.add(nums[i])
        mul=k
        while mul in s:
            mul+=k

        return mul

        