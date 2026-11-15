class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        ans=0
        pref=[0]*n
        mod=1000000007
        pref[0]=arr[0]
        for i in range(1,n):
            pref[i]=pref[i-1]+arr[i]
        odd=0
        even=0
        for i in range(n):
            if(pref[i]%2==0):
                even+=1
                ans+=odd
            else:
                odd+=1
                ans+=even+1
        return ans%mod




        