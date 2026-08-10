class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        c=0
        n=len(arr)
        """for i in range(n):
            s=0
            for j in range(i,n):
                s+=arr[j]
                if((j-i+1)==k and s//(j-i+1)>=threshold):
                    c+=1
        return c"""
        s=0
        for i in range(k):
            s+=arr[i]
        avg=s//k
        if(avg>=threshold):
            c=1
        for i in range(k,n):
            s-=arr[i-k]
            s+=arr[i]
            if(s//k>=threshold):
                c+=1
        return c
        