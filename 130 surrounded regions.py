class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        current = [(i,j) for i in range(len(board)) for j in (0, len(board[0])-1)] 
        current+= [(i,j) for i in (0, len(board)-1) for j in range(1,len(board[0])-1)]
        #print current
        while current:
            i, j = current.pop()
            visited[i][j] = True
            if board[i][j] == 'O':
                board[i][j] = 'C'
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<len(board) and 0<=y<len(board[0]) and visited[x][y] is False:
                        visited[x][y] = True
                        current.append((x, y))
        mapping = {'X':'X', 'O':'X', 'C':'O'}
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = mapping[board[i][j]]

input1=["XXXX","XOOX","XXOX","XOXX"]
board1=[]
for item in input1: board1.append([c for c in item])

a=Solution()
a.solve(board1)
print board1