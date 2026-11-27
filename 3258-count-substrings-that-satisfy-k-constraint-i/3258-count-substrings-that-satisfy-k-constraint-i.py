class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans=0
        r=0
        l=0
        n=len(s)
        oc=0
        zc=0
        for r in range(0,n):
            if(s[r]=='1'):
                oc+=1
            else:
                zc+=1
            while zc>k and oc>k:
                if(s[l]=='1'):
                    oc-=1
                else:
                    zc-=1
                l+=1
            ans+=(r-l+1)
        return ans


        