def selfdividing(n):
    num=str(n)
    if("0" in num):
        return False
    for i in range(len(num)):
        if(n%int(num[i])!=0):
            return False
    return True
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans=[]
        for i in range(left,right+1):
            if(selfdividing(i)):
                ans.append(i)
        return ans
        