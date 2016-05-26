class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix=matrix
        self.res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.bt(i,j,[])
        #print self.res
        return len(self.res)
        
    def bt(self,i,j,tmp):
        if len(tmp)>len(self.res): self.res=tmp[:]
        if i<0 or j<0 or i>=len(self.matrix) or j>=len(self.matrix[0]): return
        if not tmp or self.matrix[i][j]>tmp[-1]:
            self.bt(i+1,j,tmp+[self.matrix[i][j]])
            self.bt(i-1,j,tmp+[self.matrix[i][j]])
            self.bt(i,j+1,tmp+[self.matrix[i][j]])
            self.bt(i,j-1,tmp+[self.matrix[i][j]])

class Solution1(object): # topological sort DFS
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        self.matrix=matrix
        self.h,self.w = len(matrix),len(matrix[0])

        self.dp = [[0]*self.w for x in range(self.h)]
        print self.dp
        for x in range(self.h):
            for y in range(self.w):
                if not self.dp[x][y]: self.dfs(x,y)
        #print self.dp
        return max([max(x) for x in self.dp])
        
    def dfs(self,x, y):
        for dx,dy in zip([1,0,-1,0], [0,1,0,-1]):
            nx,ny = x+dx,y+dy
            if 0<=nx<self.h and 0<=ny<self.w and self.matrix[nx][ny]>self.matrix[x][y]:
                if not self.dp[nx][ny]: self.dfs(nx,ny)
                self.dp[x][y] = max(self.dp[x][y], self.dp[nx][ny]+1)
        self.dp[x][y] = max(self.dp[x][y],1)
        
class Solution2(object): # topological sort BFS
    def longestIncreasingPath(self,matrix):
        if not matrix: return 0
        n,m=len(matrix),len(matrix[0])
        mp ={(x,y):[] for x in range(n) for y in range(m)} #prereqs
        mp2={(x,y):[] for x in range(n) for y in range(m)} #deps
        
        for x in range(n):
            for y in range(m):
                for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if not (0<=nx<n and 0<=ny<m): continue
                    if matrix[nx][ny]>matrix[x][y]: 
                        mp[(nx,ny)].append((x,y))
                        mp2[(x,y)].append((nx,ny))
        
        dp = [[0]*m for x in range(n)]
        cur=[x for x in mp if mp[x]==[]]
        k=1
        while cur:
            nxt=[]
            for a in cur:
                x,y=a
                dp[x][y]=k
                for b in mp2[a]:
                    mp[b].remove(a)
                    if mp[b]==[]: nxt.append(b)
            k+=1
            cur=nxt
        return max([max(x) for x in dp])
                
        
matrix1=[[9,9,4],
         [6,6,8],
         [2,1,1]]
matrix2=[[3,4,5],
         [3,2,6],
         [2,2,1]]  
a=Solution2()
print a.longestIncreasingPath(matrix1) #4
print a.longestIncreasingPath(matrix2) #4