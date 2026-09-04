class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        idx=[]
        for i in range(len(s)):
            if(s[i]==c):
                idx.append(i)
        ans=[]
        for i in range(len(s)):
            mini=float('inf')
            for j in range(len(idx)):
                d=abs(i-idx[j])
                if(d<mini):
                    mini=d
            ans.append(mini)
        return ans
        