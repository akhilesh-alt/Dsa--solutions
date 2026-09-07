class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        p1=0
        p2=n-1
        ans=list(s)
        while p1<p2:
            if not ans[p1].isalpha():
                p1+=1
            elif not ans[p2].isalpha():
                p2-=1
            else:
                ans[p1],ans[p2]=ans[p2],ans[p1]
                p1+=1
                p2-=1
        return "".join(ans)


        