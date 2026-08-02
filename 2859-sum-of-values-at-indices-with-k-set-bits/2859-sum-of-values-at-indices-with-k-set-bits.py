class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        indices=[]
        n=len(nums)
        for i in range(n):
            num=i
            st=[]
            while num!=0:
                r=num%2
                st.append(r)
                num//=2
            s=str(st)
            c=0
            for j in range(len(s)):
                if(s[j]=='1'):
                    c+=1
            if(c==k):
                indices.append(i)
        ans=0
        for num in indices:
            ans+=nums[num]
        return ans
        

        



    
        