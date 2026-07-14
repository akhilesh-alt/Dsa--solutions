class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bs=[]
        while num>0:
            r=num%2
            bs.append(r)
            num//=2
        bs.reverse()
        com=[]
        for i in range(len(bs)):
            if(bs[i]==0):
                com.append("1")
            else:
                com.append("0")
        newb="".join(com)
        ans=0
        for ch in newb:
            ans=(ans*2)+int(ch)
        return ans
        

        