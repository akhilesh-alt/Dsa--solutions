def solve(n,ls,cob,ccb,ans):
    if(len(ls)==n):
        ans.append("".join(ls))
        return 
    if(cob<n//2):
        ls.append('(')
        solve(n,ls,cob+1,ccb,ans)
        ls.pop()
    if(cob>ccb):
        ls.append(')')
        solve(n,ls,cob,ccb+1,ans)
        ls.pop()
    


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        solve(2*n,[],0,0,ans)
        return ans

        