class Solution(object): #DFS
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        self.grid=grid
        self.n,self.m=len(grid),len(grid[0])
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(i,j): res+=1
        return res
        
    def dfs(self,i,j):
        if self.grid[i][j]!='1': return False
        self.grid[i][j]='3'      #visited
        for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=ni<self.n and 0<=nj<self.m:
                self.dfs(ni,nj)  #void return
        return True
    
input1=["11110",
        "11010",
        "11000",
        "00000"]
grid1=[]
for item in input1: grid1.append([c for c in item])

input2=["11000",
        "11000",
        "00100",
        "00011"]
grid2=[]
for item in input2: grid2.append([c for c in item])

a=Solution()
print a.numIslands(grid1) #1
print a.numIslands(grid2) #3