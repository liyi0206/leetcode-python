class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n=n
        self.res = []
        self.bt(0,[]) #void
        return self.res  
    
    def bt(self,i,tmp):
        if i == self.n:
            self.res.append(map(lambda x: '.'*x+"Q"+'.'*(self.n-x-1), tmp))
        for j in range(self.n):
            if j not in tmp and self.diag_legal(tmp,i,j):
                self.bt(i+1,tmp+[j])

    def diag_legal(self,tmp,row, col):
        for i in range(len(tmp)):
            if abs(row-i) == abs(col-tmp[i]):
                return False
        return True

a=Solution()
print a.solveNQueens(4)