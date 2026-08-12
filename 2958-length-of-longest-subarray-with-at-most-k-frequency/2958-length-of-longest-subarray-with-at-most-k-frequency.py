class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        p1=0
        p2=0
        ans=0
        freq={}
        while p2<n:
            freq[nums[p2]]=freq.get(nums[p2],0)+1
            while freq[nums[p2]]>k:
                freq[nums[p1]]-=1
                p1+=1
            ans=max(ans,(p2-p1+1))
            p2+=1
        return ans


        