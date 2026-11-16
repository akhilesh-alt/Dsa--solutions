class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n=len(s)
        while len(s)>k:
            ans=""
            for i in range(0,len(s),k):
                g=s[i:i+k]
                su=0
                for ch in g:
                    su+=int(ch)
                ans+=str(su)
            s=ans
        return s

            

        

        