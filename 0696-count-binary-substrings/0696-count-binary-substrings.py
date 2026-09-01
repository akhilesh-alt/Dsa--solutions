class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """n=len(s)
        ans=0
        for i in range(n):
            oc=0
            zc=0
            ch=0
            for j in range(i,n):
                if(s[j]=='1'):
                    oc+=1
                else:
                    zc+=1
                if(j>i and s[j]!=s[j-1]):
                    ch+=1
                if(oc==zc and ch==1):
                    ans+=1
        return ans"""
        n=len(s)
        gs=[]
        p1=0
        p2=1
        ans=0
        while p2<n:
            if(s[p2]!=s[p2-1]):
                gs.append(p2-p1)
                p1=p2
                p2+=1
            else:
                p2+=1
        gs.append(n-p1)
        for i in range(0,len(gs)-1):
            ans+=min(gs[i],gs[i+1])
        return ans
