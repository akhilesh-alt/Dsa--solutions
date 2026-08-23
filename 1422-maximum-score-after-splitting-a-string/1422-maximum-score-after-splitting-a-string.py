class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones=0
        for i in range(len(s)):
            if(s[i]=='1'):
                ones+=1
        ans=0
        lz=0
        ro=ones
        for i in range(len(s)-1):
            if(s[i]=='0'):
                lz+=1
            else:
                ro-=1
            score=lz+ro
            ans=max(ans,score)
        return ans


        