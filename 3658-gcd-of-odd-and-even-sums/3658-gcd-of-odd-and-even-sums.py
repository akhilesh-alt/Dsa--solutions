class Solution(object):
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        so=0
        se=0
        so=(n*n)
        se=n*(n+1)
        return self.gcd(so,se)


        