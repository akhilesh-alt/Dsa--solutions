class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        ans=-1
        if(k==1):
            mp={}
            for i in range(n):
                mp[nums[i]]=mp.get(nums[i],0)+1
            for ke in mp.keys():
                if(mp[ke]==1):
                    ans=max(ans,ke)
            return ans
        if(k==n):
            return max(nums)
        if(k>1 and k<n):
            a1=0
            a2=0
            for i in range(n):
                if(nums[i]==nums[0]):
                    a1+=1
                if(nums[i]==nums[n-1]):
                    a2+=1
            if(a1==1 and a2==1):
                return max(nums[0],nums[n-1])
            if(a1==1):
                return nums[0]
            if(a2==1):
                return nums[n-1]
        return -1




        