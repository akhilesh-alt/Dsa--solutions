class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        bs=[]
        if(n==0):
            return 1
        while n>0:
            r=n%2
            if(r==0):
                bs.append(1)
            else:
                bs.append(0)
            n//=2
        ans=0
        for i in range(len(bs)-1,-1,-1):
            ans=ans*2+bs[i]
        return ans

            


        