class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        ans=[0]*n
        if(k==0):
            for i in range(n):
                ans[i]=0
        elif(k>0):
            s=0
            for i in range(n):
                s=0
                for j in range(i+1,i+k+1):
                    s+=code[j%n]
                ans[i]=s
        elif(k<0):
            s=0
            for i in range(n):
                s=0
                for j in range(i+k,i):
                    s+=code[j%n]
                ans[i]=s
        return ans



        