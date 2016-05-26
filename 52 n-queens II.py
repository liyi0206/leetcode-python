class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n=n
        self.res = 0
        self.bt(0,[]) #void
        return self.res
    
    def bt(self,i,tmp):
        if i == self.n:
            self.res +=1
        for j in range(self.n):
            if j not in tmp and self.diag_legal(tmp,i,j):
                self.bt(i+1,tmp+[j])

    def diag_legal(self,tmp,row, col):
        for i in range(len(tmp)):
            if abs(row-i) == abs(col-tmp[i]):
                return False
        return True

a=Solution()
print a.totalNQueens(4)
print a.totalNQueens(8)