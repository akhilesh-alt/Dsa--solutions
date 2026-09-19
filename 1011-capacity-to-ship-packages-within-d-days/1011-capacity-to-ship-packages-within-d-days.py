class Solution(object):
    def check(self,weights,days,m,l,h,n):
        s=0
        c=1
        for i in range(n):
            s+=weights[i]
            if(s>m):
                c+=1
                s=weights[i]
        if(c<=days):
            return True
        return False

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        n=len(weights)
        l=max(weights)
        s=0
        for i in range(n):
            s+=weights[i]
        h=s
        ans=float('inf')
        while l<=h:
            m=(l+h)//2
            if(self.check(weights,days,m,l,h,n)):
                ans=m
                h=m-1
            else:
                l=m+1
        return ans
        