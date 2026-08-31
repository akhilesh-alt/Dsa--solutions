class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        cnt=0
        c=start^goal
        while c>0:
            if(c%2==1):
                cnt+=1
            c/=2
        return cnt
        
        
        
        