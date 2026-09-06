class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        p1=0
        p2=n-1
        while p1<p2:
            if(nums[p1]%2==0):
                p1+=1
            elif(nums[p2]%2!=0):
                p2-=1
            else:
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p2-=1
                p1+=1
        return nums
        