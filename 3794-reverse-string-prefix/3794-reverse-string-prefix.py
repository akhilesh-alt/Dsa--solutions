class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s1=[]
        for i in range(k):
            s1.append(s[i])
        s1.reverse()
        s11="".join(s1)
        s2=[]
        for i in range(k,len(s)):
            s2.append(s[i])
        s22="".join(s2)
        ans=s11+s22
        return ans
        