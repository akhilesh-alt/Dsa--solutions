class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s1=[]
        idx=-1
        for i in range(len(word)):
            if(word[i]==ch):
                idx=i
                break
        s1=word[0:idx+1]
        s2=word[idx+1:len(word)]
        ls=list(s1)
        ls.reverse()
        s11="".join(ls)
        res=s11+s2
        return res


        