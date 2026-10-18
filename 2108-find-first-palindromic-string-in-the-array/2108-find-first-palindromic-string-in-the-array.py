def check(s):
    p1=0
    p2=len(s)-1
    while p1<p2:
        if(s[p1]!=s[p2]):
            return False
        p1+=1
        p2-=1
    return True
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        n=len(words)
        ans=""
        for i in range(n):
            if(check(words[i])):
                ans=words[i]
                break
        return ans

        