class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen=set()
        ans=[]
        curr=""
        for ch in s:
            curr+=ch
            if curr not in seen:
                seen.add(curr)
                ans.append(curr)
                curr=""
        return ans
        