class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j]=grid[i][j]
                
        for i in range(1,len(grid)): res[i][0] += res[i-1][0]
        for j in range(1,len(grid[0])): res[0][j] += res[0][j-1]
        for i in range(1,len(res)):
            for j in range(1,len(res[0])):
                res[i][j] += min(res[i-1][j], res[i][j-1])
        return res[len(res) - 1][len(res[0]) - 1]
        
grid=[[2,1,3],[7,6,5],[4,8,9]]
a=Solution()
print a.minPathSum(grid)