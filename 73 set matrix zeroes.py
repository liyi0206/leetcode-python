class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        frow,fcol = 0,0
        for k in range(len(matrix[0])):
            if matrix[0][k] == 0: frow =1
        for k in range(len(matrix)):
            if matrix[k][0] == 0: fcol =1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j],matrix[i][0]=0,0
        #print frow,fcol,matrix
                    
        for k in range(1,len(matrix[0])):
            if matrix[0][k] == 0:
                for n in range(len(matrix)):
                    matrix[n][k]=0
        #print matrix
        for k in range(1,len(matrix)):
            if matrix[k][0] == 0:
                for n in range(len(matrix[0])):
                    matrix[k][n]=0
        #print matrix
        if frow==1:
            for n in range(len(matrix[0])):
                matrix[0][n]=0
        if fcol==1:
            for n in range(len(matrix)):
                matrix[n][0]=0
        
a=Solution()
#matrix=[[1,2,3],[4,0,6],[7,8,9]]
#a.setZeroes(matrix)
#print matrix

#matrix=[[1,2,0],[4,0,6],[7,8,9]]
#a.setZeroes(matrix)
#print matrix

matrix=[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
a.setZeroes(matrix)
print matrix