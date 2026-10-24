class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=set()
        c=0
        for ch in jewels:
            s.add(ch)
        for i in range(len(stones)):
            if(stones[i] in s):
                c+=1
        return c
        