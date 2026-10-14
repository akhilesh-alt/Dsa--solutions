def solve(n,k,a,dp):
    if(k==0):
        return 1
    if(n==0):
        return 0
    if(dp[n][k]!=-1):
        return dp[n][k]
    up=solve(n-1,k,a,dp)
    p=0
    if(k-a[n-1]>=0):
        p=solve(n,k-a[n-1],a,dp)
    dp[n][k]=p+up
    return dp[n][k]
    
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        k=amount
        n=len(coins)
        dp=[[-1]*(k+1) for _ in range(n+1)]
        return solve(n,k,coins,dp)

        