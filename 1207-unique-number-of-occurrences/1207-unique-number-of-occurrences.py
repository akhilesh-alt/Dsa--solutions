class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        n=len(arr)
        freq={}
        for i in range(n):
            freq[arr[i]]=freq.get(arr[i],0)+1
        s=set()
        for val in freq.values():
            if(val in s):
                return False
            s.add(val)
        return True
