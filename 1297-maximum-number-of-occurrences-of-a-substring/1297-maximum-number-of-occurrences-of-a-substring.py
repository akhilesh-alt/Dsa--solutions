class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        mp={}
        ans=0
        for i in range(len(s)-minSize+1):
            ss=s[i:i+minSize]
            if(len(set(ss))<=maxLetters):
                mp[ss]=mp.get(ss,0)+1
        for k in mp.keys():
            ans=max(ans,mp[k])
        return ans
            
        




        