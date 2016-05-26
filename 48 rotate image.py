#class Solution(object):
#    def rotate(self, matrix):
#        """
#        :type matrix: List[List[int]]
#        :rtype: void Do not return anything, modify matrix in-place instead.
#        [[1,2],[3,4]] --> [[3,1],[4,2]]
#        [[1,2,3],[4,5,6],[7,8,9]] --> [[7,4,1],[8,5,2],[9,6,3]]
#        """
#        n=len(matrix)
#        res=[[0 for i in range(n)] for i in range(n)]
#        for i in range(n):
#            for j in range(n):
#                res[j][n-i-1]=matrix[i][j]
#        return res
        
class Solution(object):
    def rotate(self, matrix):
        """
        [0][0]->[0][n-1]->[n-1][n-1]->[n-1][0]->[0][0]
        [0][1]->...
        """
        n=len(matrix)
        for i in range(n/2):
            for j in range(i,n-1-i):
                matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i],matrix[i][j] = \
                matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i]
        #return matrix
        #print matrix