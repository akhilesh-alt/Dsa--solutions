class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a1=[]
        a2=[]
        n=len(nums)
        a1.append(nums[0])
        a2.append(nums[1])
        res=[]
        for i in range(2,n):
            if(a1[len(a1)-1]>a2[len(a2)-1]):
                a1.append(nums[i])
            else:
                a2.append(nums[i])
        for i in range(len(a1)):
            res.append(a1[i])
        for i in range(len(a2)):
            res.append(a2[i])
        return res
        
        