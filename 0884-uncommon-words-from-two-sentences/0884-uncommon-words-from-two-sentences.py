class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words=s1.split()+s2.split()
        freq={}
        for w in words:
            freq[w]=freq.get(w,0)+1
        ans=[]
        for w in freq:
            if(freq[w]==1):
                ans.append(w)
        return ans        