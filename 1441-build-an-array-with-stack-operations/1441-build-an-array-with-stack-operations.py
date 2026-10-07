class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        k=len(target)
        ans=[]
        for i in range(1,n+1):
            if(i in target):
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
            if i == target[-1]:
                break
        return ans

        