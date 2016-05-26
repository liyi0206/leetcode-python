class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix==[] or matrix[0]==[]: return
        self.matrix=matrix
        self.n,self.m = len(matrix),len(matrix[0])
        
        self.tree = [[0]*(self.m+1) for i in range(self.n+1)]
        for i in range(self.n):
            for j in range(self.m):
                self.add(i+1,j+1,matrix[i][j])
        #for l in self.tree: print l

    def lowbit(self,x):
        return x&(-x)
        
    def add(self,x,y,val):
        while x<=self.n:
            z=y
            while z<=self.m:
                self.tree[x][z]+=val
                z+=self.lowbit(z)
            x+=self.lowbit(x)
            
    def sum(self,x,y):
        res=0
        while x>0:
            z=y
            while z>0:
                res+=self.tree[x][z]
                z-=self.lowbit(z)
            x-=self.lowbit(x)
        #print res
        return res
        
    def update(self,row,col,val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.add(row+1,col+1,val-self.matrix[row][col])
        self.matrix[row][col]=val

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix: return 0
        return self.sum(row2+1,col2+1) \
              -self.sum(row1,col2+1) \
              -self.sum(row2+1,col1) \
              +self.sum(row1,col1)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]]
numMatrix=NumMatrix(matrix)
print numMatrix.sumRegion(2,1,4,3) #8
numMatrix.update(3,2,2)
print numMatrix.sumRegion(2,1,4,3) #10