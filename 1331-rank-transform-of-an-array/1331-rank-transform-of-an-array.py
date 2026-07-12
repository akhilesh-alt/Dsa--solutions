class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """n=len(arr)
        tem=[]
        for i in range(n):
            tem.append(arr[i])
        tem.sort()
        ans=[0]*n
        
        for i in range(n):
            s=set()
            for j in range(n):
                if(tem[j]<arr[i]):
                    s.add(tem[j])
            r=len(s)+1
            ans[i]=r
        return ans"""
        n=len(arr)
        tem=[]
        for i in range(n):
            tem.append(arr[i])
        tem.sort()
        rank={}
        r=1
        for i in range(n):
            if tem[i] not in rank:
                rank[tem[i]]=r
                r+=1
        ans=[]
        for i in range(n):
            ans.append(rank[arr[i]])
        return ans


            


        