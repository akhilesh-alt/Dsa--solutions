class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st=[]
        dic={}
        for i in range(len(nums2)):
            while len(st)>0 and nums2[i]>st[-1]:
                dic[st[-1]]=nums2[i]
                st.pop()
            st.append(nums2[i])
        ans=[]
        for x in nums1:
            ans.append(dic.get(x,-1))
        return ans

        
        
        


        