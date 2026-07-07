class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        x=[]
        for i in range(len(s)):
            if(s[i]!="0"):
                x.append(s[i])
        newnum="".join(x)
        summ=0
        for i in range(len(x)):
            summ+=int(x[i])
        if(newnum==""):
            return 0
        return summ*int(newnum)




        