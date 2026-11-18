class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)
        sett=set()
        c=0
        for i in range(0,n-1,2):
            ss=s[i:i+2]
            if(ss[0]!=ss[1]):
                c+=1
        return c


        

        