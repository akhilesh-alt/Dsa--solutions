class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        p1=0
        p2=0
        ans=0
        freq={}
        while p2<n:
            freq[s[p2]]=freq.get(s[p2],0)+1
            while freq[s[p2]]>2:
                freq[s[p1]]-=1
                p1+=1
            ans=max(ans,(p2-p1+1))
            p2+=1
        return ans


            

        