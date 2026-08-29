class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        li=-1
        c=0
        p1=0
        p2=0
        ans=""
        while p2<len(s):
            if(s[p2]=='1'):
                c+=1
            while c>k:
                if(s[p1]=='1'):
                    c-=1
                p1+=1
            if c == k:
                while s[p1] == '0':
                    p1 += 1

                curr = s[p1:p2 + 1]
                if (ans == "" or
                    len(curr) < len(ans) or
                    (len(curr) == len(ans) and curr < ans)):
                    ans = curr

            p2 += 1
        return ans
        
        
        