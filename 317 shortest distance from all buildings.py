class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return None
        n,m=len(grid),len(grid[0])
        
        for a in range(n):
            for b in range(m):
                grid[a][b]=-grid[a][b]
        matrix=[l[:] for l in grid]
        
        bldgs=[(i,j) for i in range(n) for j in range(m) if grid[i][j]==-1]
        for i,j in bldgs:
            #print (i,j)
            visited=[l[:] for l in matrix]

            k=0
            cur=set([(i,j)])
            while cur:
                k+=1
                nxt=set()
                for (i,j) in cur:
                    for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if 0<=x<n and 0<=y<m and visited[x][y]==0:
                            visited[x][y]=k
                            grid[x][y] +=k
                            nxt.add((x,y))
                cur=nxt
            #for l in visited: print l
            #print
            #for l in grid: print l
            #print
            for a in range(n):
                for b in range(m):
                    if visited[a][b]==0: 
                        matrix[a][b]=-3
                        grid[a][b]=-3
        res=1000000
        for a in range (n):
            for b in range(m):
                if grid[a][b]>0: res=min(res,grid[a][b])
        return res if res<1000000 else -1
        
        
grid=[[1,0,2,0,1],
      [0,0,0,0,0],
      [0,0,1,0,0]]
a=Solution()
print a.shortestDistance(grid) #7

grid=[[0,2,1],
      [1,0,2],
      [0,1,0]]
a=Solution()
print a.shortestDistance(grid) #-1

grid=[[1,1,1,1,1,0],
      [0,0,0,0,0,1],
      [0,1,1,0,0,1],
      [1,0,0,1,0,1],
      [1,0,1,0,0,1],
      [1,0,0,0,0,1],
      [0,1,1,1,1,0]]
a=Solution()
print a.shortestDistance(grid) #88

grid=[[1,1],[0,1]]
a=Solution()
print a.shortestDistance(grid) #-1