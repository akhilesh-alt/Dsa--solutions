class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans=[]
        n=len(arr2)
        freq={}
        for i in range(len(arr1)):
            freq[arr1[i]]=freq.get(arr1[i],0)+1
        ans=[]
        remain=[]
        for i in range(len(arr2)):
            if(arr2[i] in freq):
                c=freq.get(arr2[i])
                while c>0:
                    ans.append(arr2[i])
                    c-=1
                freq[arr2[i]]=0
            
        for i in range(len(arr1)):
            if(freq[arr1[i]]>0):
                remain.append(arr1[i])
                freq[arr1[i]]-=1
        remain.sort()
        return ans+remain