class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """n=len(nums)
        c=0
        for i in range(n):
            cn=0
            for j in range(i,n):
                if(nums[j]%2!=0):
                    cn+=1
                if(cn==k):
                    c+=1
        return c"""
        n=len(nums)
        ps=[-1]*n
        for i in range(n):
            if(nums[i]%2==0):
                ps[i]=0
            else:
                ps[i]=1
        for i in range(1,n):
            ps[i]=ps[i-1]+ps[i]
        freq={0:1}
        ans=0
        for i in range(n):
            if ps[i]-k in freq:
                ans+=freq[ps[i]-k]
            if ps[i] in freq:
                freq[ps[i]]+=1
            else:
                freq[ps[i]]=1
        return ans
        


        
        