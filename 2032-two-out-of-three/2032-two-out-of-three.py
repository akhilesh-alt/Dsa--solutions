class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        s1=set()
        s2=set()
        s3=set()
        n1=len(nums1)
        n2=len(nums2)
        n3=len(nums3)
        for i in range(n1):
            s1.add(nums1[i])
           
        for i in range(n2):
            s2.add(nums2[i])
            
        for i in range(n3):
            s3.add(nums3[i])
        ans=(s1&s2)|(s2&s3)|(s1&s3)
        return list(ans)
        

        
        