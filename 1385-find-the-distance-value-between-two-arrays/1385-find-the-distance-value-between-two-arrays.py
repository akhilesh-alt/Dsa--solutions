class Solution(object):
    def bs(self,arr2,k,d):
        l=0
        h=len(arr2)-1
        while l<=h:
            m=(l+h)//2
            if(abs(arr2[m]-k)<=d):
                return 1
            elif(arr2[m]>k):
                h=m-1
            else:
                l=m+1
        return 0
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n1=len(arr1)
        n2=len(arr2)
        arr2.sort()
        ans=0
        for i in range(n1):
            if self.bs(arr2,arr1[i],d)==0:
                ans+=1
        return ans
        

        