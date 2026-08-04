class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        maxi=max(nums)
        mini=min(nums)
        res=[]
        for i in range(mini,maxi+1):
            if(i not in nums):
                res.append(i)
        res.sort()
        return res

            
        