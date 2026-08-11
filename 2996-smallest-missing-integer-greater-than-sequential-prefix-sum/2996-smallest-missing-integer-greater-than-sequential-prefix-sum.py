class Solution(object):
    def bs(self,sl,l,h,x):
        while l<=h:
            m=(l+h)//2
            if(sl[m]==x):
                return True
            elif(sl[m]>x):
                h=m-1
            else:
                l=m+1
        return False
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        idx=n-1
        for i in range(1,n):
            if(nums[i]!=nums[i-1]+1):
                idx=i-1
                break
        sl=[]
        for i in range(n):
            sl.append(nums[i])
        sl.sort()
        ps=0
        for i in range(0,idx+1):
            ps+=nums[i]
        while self.bs(sl,0,len(sl)-1,ps)==True:
            ps+=1
        
        return ps
        

        