class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        m=l//2
        if(l%2==0):
            fh=s[0:m]
            fhl=list(fh)
            fhl.sort()
            fhh="".join(fhl)
            fhl.reverse()
            shh="".join(fhl)
            ns=fhh+shh
        else:
            fh=s[0:m]
            mp=s[m]
            fhl=list(fh)
            fhl.sort()
            fhh="".join(fhl)
            fhl.reverse()
            shh="".join(fhl)
            ns=fhh+mp+shh
        return ns
        


        