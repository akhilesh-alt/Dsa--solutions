class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        expected=[]
        for num in heights:
            expected.append(num)
        expected.sort()
        c=0
        for i in range(n):
            if(heights[i]!=expected[i]):
                c+=1
        return c
        