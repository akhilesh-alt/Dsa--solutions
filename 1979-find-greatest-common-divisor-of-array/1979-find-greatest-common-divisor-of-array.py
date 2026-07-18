class Solution(object):
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
        
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        a=min(nums)
        b=max(nums)
        return self.gcd(a,b)

        