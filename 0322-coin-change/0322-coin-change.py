def solve(a,n,k,dp):
    if(k==0):
        return 0
    if(n<0):
        return float('inf')
    if(dp[n][k]!=-1):
        return dp[n][k]
    np=solve(a,n-1,k,dp)
    p=float('inf')
    if(k-a[n]>=0):
        res=solve(a,n,k-a[n],dp)
        if(res!=float('inf')):
            p=1+res
    dp[n][k]=min(p,np)
    return dp[n][k]
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        k=amount
        n=len(coins)
        dp=[[-1]*(k+1) for _ in range(n+1)]
        ans=solve(coins,n-1,k,dp)
        if(ans!=float('inf')):
            return ans
        return -1
        