class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        c=0
        for row in grid:
            l=0
            h=len(row)-1
            while l<=h:
                m=(l+h)//2
                if(row[m]<0):
                    h=m-1
                else:
                    l=m+1
            c+=len(row)-l
        return c