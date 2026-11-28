def isvowel(ch):
    if(ch in ['a','e','i','o','u']):
        return True
    else:
        return False
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        m=len(s)//2
        a=s[0:m]
        b=s[m:]
        f=0
        l=0
        for i in range(len(a)):
            if(isvowel(a[i])):
                f+=1
        for i in range(len(b)):
            if(isvowel(b[i])):
                l+=1
        if(f==l):
            return True
        return False




        