class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        n=len(words)
        mp={}
        ans=[]
        for ch in words[0]:
            mp[ch]=mp.get(ch,0)+1
        for ch in mp:
            t=min(w.count(ch) for w in words)
            while t>0:
                ans.append(ch)
                t-=1
        return ans


        
        