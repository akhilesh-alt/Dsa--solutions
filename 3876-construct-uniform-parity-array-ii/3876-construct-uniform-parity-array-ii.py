class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n=len(nums1)
        odd=[]
        even=[]
        for i in range(n):
            if(nums1[i]%2==0):
                even.append(nums1[i])
            else:
                odd.append(nums1[i])
        if(len(even)==0):
            return True
        if(len(odd)==0):
            return True
        if(min(odd)<min(even)):
            return True
        return False
        