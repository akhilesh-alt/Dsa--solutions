class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=list(s.split())
        res=[]
        for i in range(len(a)):
            w=a[i]
            ls=list(w)
            ls.reverse()
            nw="".join(ls)
            res.append(nw)
        return " ".join(res)

    