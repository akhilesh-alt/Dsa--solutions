class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        ans=""
        for i in range(n):
            p1=i
            p2=i
            while p1>=0 and p2<n:
                if(s[p1]==s[p2]):
                    p1-=1
                    p2+=1
                else:
                    break
            curr=s[p1+1:p2]
            if(len(curr)>len(ans)):
                ans=curr
            p1=i
            p2=i+1
            while p1>=0 and p2<n:
                if(s[p1]==s[p2]):
                    p1-=1
                    p2+=1
                else:
                    break
            cur=s[p1+1:p2]
            if(len(cur)>len(ans)):
                ans=cur
        return ans
                
        

        