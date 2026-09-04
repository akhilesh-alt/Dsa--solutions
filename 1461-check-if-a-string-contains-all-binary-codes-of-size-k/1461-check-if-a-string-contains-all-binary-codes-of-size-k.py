class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        seen=set()
        ss=[]
        if(k>len(s)):
            return False
        for i in range(0,k):
            ss.append(s[i])
        seen.add("".join(ss))
        for i in range(k,len(s)):
            ss.pop(0)
            ss.append(s[i])
            seen.add("".join(ss))
        if(len(seen)==2**k):
            return True
        return False




        