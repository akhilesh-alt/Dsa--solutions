class Solution(object):
    def check(self,piles,m,h,low,high):
        s=0
        for i in range(len(piles)):
            s+=(piles[i]+m-1)//m
        if(s<=h):
            return True
        return False

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n=len(piles)
        low=1
        high=max(piles)
        ans=float('inf')
        while low<=high:
            m=(low+high)//2
            if(self.check(piles,m,h,low,high)):
                ans=m
                high=m-1
            else:
                low=m+1
        return ans
        