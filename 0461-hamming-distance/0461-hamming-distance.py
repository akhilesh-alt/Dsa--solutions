class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bs1=[]
        while x>0:
            r=x%2
            bs1.append(r)
            x//=2
        bs1.reverse()
        idx=32-len(bs1)
        fp=[]
        for i in range(0,idx):
            fp.append(0)
        fp1="".join(map(str,fp))
        fp2="".join(map(str,bs1))
        n1=fp1+fp2
        bs2=[]
        while y>0:
            r=y%2
            bs2.append(r)
            y//=2
        bs2.reverse()
        idx=32-len(bs2)
        np=[]
        for i in range(0,idx):
            np.append(0)
        np1="".join(map(str,np))
        np2="".join(map(str,bs2))
        n2=np1+np2
        n1=list(n1)
        n2=list(n2)
        c=0
        for i in range(len(n1)):
            if(n1[i]!=n2[i]):
                c+=1
        return c


        