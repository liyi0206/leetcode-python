class Solution(object):
    def solveSudoku(self, board): #o(9^m), m is the number of empty cells (<81)
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board=board
        print self.bt() # by problem def, will always return True, 
                        # as there is always one solution.
    def bt(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]=='.':
                    for k in '123456789':
                        self.board[i][j]=k
                        if self.is_valid(i,j) and self.bt():
                            return True
                        self.board[i][j]='.'
                    return False
        return True
        
    def is_valid(self,x,y):
        tmp=self.board[x][y]; self.board[x][y]='x'
        for i in range(9):
            if self.board[i][y]==tmp: return False
            if self.board[x][i]==tmp: return False
        for i in range(3):
            for j in range(3):
                if self.board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
        self.board[x][y]=tmp
        return True
        
import pprint
pp=pprint.PrettyPrinter(indent=4)
tmp=[
        '53..7....',
        '6..195...',
        '.98....6.',
        '8...6...3',
        '4..8.3..1',
        '7...2...6',
        '.6....28.',
        '...419..5',
        '....8..79'
    ]
board=[[a[j] for j in range(9)] for a in tmp]
pp.pprint(board)

a=Solution()
a.solveSudoku(board)
pp.pprint(board)