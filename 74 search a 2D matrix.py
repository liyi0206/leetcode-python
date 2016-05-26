class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        l, h = 0, len(matrix) * len(matrix[0]) - 1
        while (l <= h):
            m = l+(h-l)/2
            v = matrix[m/len(matrix[0])][m%len(matrix[0])]
            if v==target: return True
            elif v<target: l = m + 1
            else: h = m - 1
        return False