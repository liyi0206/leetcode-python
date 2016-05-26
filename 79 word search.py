class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board=board
        visited=[[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.bt(word, visited, i, j): return True
        return False
                
    def bt(self, word, visited, i, j):
        if len(word) == 0: return True
        if i<0 or j<0 or i>=len(visited) or j>=len(visited[0]) or \
           self.board[i][j] != word[0] or visited[i][j]==1:
            return False
        visited[i][j] = 1
        found = self.bt(word[1:],visited,i+1,j) or \
                self.bt(word[1:],visited,i-1,j) or \
                self.bt(word[1:],visited,i,j+1) or \
                self.bt(word[1:],visited,i,j-1)
        visited[i][j] = 0
        return found
        
class Solution2(object):
    def exist(self, board, word):
        self.board=board
        self.n,self.m=len(board),len(board[0])
        self.visited=[[0]*self.m for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if self.dfs(i,j,word): return True
        return False
        
    def dfs(self,x,y,word):
        if not word: return True     
        if self.board[x][y]==word[0] and self.visited[x][y]==0: 
            # in solution1, 0<=nx<self.n and 0<=ny<self.m is done in dfs, 
            # so (not word) case is captured. 
            if not word[1:]: return True            ###
            self.visited[x][y]=1
            for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=nx<self.n and 0<=ny<self.m:   ###
                    if self.dfs(nx,ny,word[1:]): return True
            self.visited[x][y]=0
        return False
        
class Solution3(object): # more generalizable for words search (trie)
    def exist(self, board, word):
        self.board=board
        self.n,self.m=len(board),len(board[0])
        self.visited=[[0]*self.m for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if self.dfs(i,j,word): return True
        return False
        
    def dfs(self,x,y,word):
        if not word: return True   
        if not (0<=x<self.n and 0<=y<self.m): return False
        if self.board[x][y]==word[0] and self.visited[x][y]==0: 
            self.visited[x][y]=1
            for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if self.dfs(nx,ny,word[1:]): return True
            self.visited[x][y]=0
        return False
        
board=[['A','B','C','E'],
       ['S','F','C','S'],
       ['A','D','E','E']]
a=Solution3()    
print a.exist(board,"ABCCED") #true
print a.exist(board,"SEE")    #true
print a.exist(board,"ABCB")   #false
print a.exist(["ABCE","SFCS","ADEE"],"ABCCED") #true
print a.exist(["a"],"a") #true

# only start point is independent of the previous, make it in main func. 

# remember to check visited[i][j]=1 then return False