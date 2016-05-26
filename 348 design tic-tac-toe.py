class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n=n
        self.board=[[None]*n for i in range(n)]
        self.rows,self.cols=[0]*n,[0]*n
        self.diag,self.anti=0,0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col]=player
        #for l in self.board: print l
        #print self.rows,self.cols,self.diag,self.anti
        if self.check_winner(row,col,player): return player
        else: return 0
        
    # rows and cols are initiated as 0, once added 1 or 2 at [i,j], make rows[i], 
    # cols[j] to be 1 or 2, and once a conflict, make rows[i], cols[j] to be 8 and return.
    # to know the row/col is full, still need self.board[i]==[num]*self.n.
    def check_winner(self,x,y,num):
        if self.rows[x]==0: self.rows[x]=num
        elif self.rows[x]==num: 
            if [self.board[x][i] for i in range(self.n)]==[num]*self.n: return True
        elif self.rows[x]==3-num: self.rows[x]=8
            
        if self.cols[y]==0: self.cols[y]=num
        elif self.cols[y]==num:
            if [self.board[i][y] for i in range(self.n)]==[num]*self.n: return True
        elif self.cols[y]==3-num: self.cols[y]=8

        if x==y:
            if self.diag==0: self.diag=num
            elif self.diag==3-num: self.diag=8
            elif self.diag==num:
                if [self.board[i][i] for i in range(self.n)]==[num]*self.n: return True
        if x==self.n-1-y:
            if self.anti==0: self.anti=num
            elif self.anti==3-num: self.anti=8
            elif self.anti==num:
                if [self.board[i][self.n-1-i] for i in range(self.n)]==[num]*self.n: return True
        return False
        
class TicTacToe2(object): #better solution, same time complexity, o(n) space
    def __init__(self,n):#solution1 need o(n^2) space. also check and add use same time.
        self.n=n
        self.rows,self.cols=[0]*n,[0]*n
        self.diag,self.anti=0,0

    def move(self,x,y, player):
        num=1 if player==1 else -1
        self.rows[x]+=num
        self.cols[y]+=num
        if x==y: self.diag+=num
        if x==self.n-1-y: self.anti+=num
        for i in range(self.n):
            if abs(self.rows[i])==self.n or abs(self.cols[i])==self.n or \
               abs(self.diag)==self.n or abs(self.anti)==self.n: return player
        return 0

        
a=TicTacToe2(3)
print a.move(0,0,1)
print a.move(0,2,2)
print a.move(2,2,1)
print a.move(1,1,2)
print a.move(2,0,1)
print a.move(1,0,2)
print a.move(2,1,1) #return 1

a=TicTacToe2(2)
print a.move(0,1,1)
print a.move(1,1,2)
print a.move(1,0,1) #return 1

    #def check_winner(self,num):
    #    for i in range(self.n): 
    #        if self.board[i]==[num]*self.n: return True
    #    for j in range(self.n):
    #        if [self.board[i][j] for i in range(self.n)]==[num]*self.n: return True
    #    if [self.board[i][i] for i in range(self.n)]==[num]*self.n: return True
    #    return False