class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c=0
        n=len(colors)
        if(colors[0]!=colors[n-1] and colors[0]!=colors[1]):
            c+=1
        for i in range(1,n-1):
            if(colors[i]!=colors[i-1] and colors[i]!=colors[i+1]):
                c+=1
        if(colors[n-1]!=colors[n-2] and colors[n-1]!=colors[0]):
            c+=1
        return c

        