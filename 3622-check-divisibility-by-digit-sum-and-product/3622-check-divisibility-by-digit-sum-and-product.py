class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=str(n)
        s=0
        p=1
        for i in range(len(num)):
            s+=int(num[i])
            p*=int(num[i])
        d=s+p
        if(n%d==0):
            return True
        return False


        