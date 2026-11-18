class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)
        sett=set()
        c=0
        for i in range(0,n-1,2):
            if(s[i]!=s[i+1]):
                c+=1
        return c


        

        