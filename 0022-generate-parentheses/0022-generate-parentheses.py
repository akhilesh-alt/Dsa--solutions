class Solution(object):
    def solve(self,n,ls,cob,ccb,ans):
        if(len(ls)==n):
            ans.append("".join(ls))
            return
        if(cob<n//2):
            ls.append('(')
            self.solve(n,ls,cob+1,ccb,ans)
            ls.pop()
        if(cob>ccb):
            ls.append(')')
            self.solve(n,ls,cob,ccb+1,ans)
            ls.pop()
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        self.solve(2*n,[],0,0,ans)
        return ans

        