class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        dig=[]
        for i in range(len(s)):
            dig.append(int(s[i]))
        ans=0
        for i in range(len(dig)):
            for j in range(i+1,len(dig)):
                ans=max(ans,dig[i]*dig[j])
            
        return ans

        