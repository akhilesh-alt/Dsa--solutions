class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        ans=0
        if(n<3):
            return 0
        for i in range(1,n-1):
            if(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
                p1=i
                p2=i
                while p1>0 and arr[p1-1]<arr[p1]:
                    p1-=1
                while p2<n-1 and arr[p2+1]<arr[p2]:
                    p2+=1
                ans=max(ans,(p2-p1+1))
        return ans
                
            

        