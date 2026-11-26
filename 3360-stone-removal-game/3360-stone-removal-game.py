class Solution:
    def canAliceWin(self, n: int) -> bool:
        aw=True
        s=10
        while n>=s:
            n-=s
            s-=1
            aw=not aw
        return not aw
            
