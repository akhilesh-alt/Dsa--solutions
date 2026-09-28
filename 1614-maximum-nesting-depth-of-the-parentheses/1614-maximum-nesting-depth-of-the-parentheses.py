class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        d=0
        for ch in s:
            if(ch=='('):
                d+=1
            elif(ch==')'):
                d-=1
            ans=max(ans,d)
        return ans
            