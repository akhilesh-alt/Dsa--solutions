class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        nums=[]
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        k=k%len(nums)
        for i in range(k):
            tem=nums[len(nums)-1]
            for j in range(len(nums)-1,0,-1):
                nums[j]=nums[j-1]
            nums[0]=tem
        for i in range(m):
            for j in range(n):
                idx=(i*n)+j
                r=idx//n
                c=idx%n
                grid[r][c]=nums[idx]
        return grid

        