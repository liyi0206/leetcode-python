class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.sums = [[0]*n for x in range(m)]
        for x in range(m):
            rowSum = 0
            for y in range(n):
                rowSum+=matrix[x][y]
                self.sums[x][y]=self.sums[x-1][y]+rowSum
        print self.sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0: return self.sums[row2][col2]
        elif row1==0: return self.sums[row2][col2]-self.sums[row2][col1-1]
        elif col1==0: return self.sums[row2][col2]-self.sums[row1-1][col2]
        else: return self.sums[row2][col2]+self.sums[row1-1][col1-1] \
                   - self.sums[row2][col1-1]-self.sums[row1-1][col2]


# Your NumMatrix object will be instantiated and called as such:
matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
         ]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2,1,4,3) #8
print numMatrix.sumRegion(1,1,2,2) #11
print numMatrix.sumRegion(1,2,2,4) #12
"""
[
    [ 3,  3,  4,  8, 10], 
    [ 8, 14, 18, 24, 27], 
    [ 9, 17, 21, 28, 36], 
    [13, 22, 26, 34, 49], 
    [14, 23, 30, 38, 58]
]
"""

matrix=[[-1]]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(0,0,0,0)