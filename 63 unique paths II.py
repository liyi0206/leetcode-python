class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        res = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1: break
            else: res[i][0] = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1: break
            else: res[0][i] = 1
            
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i][j-1] + res[i-1][j]
        return res[len(res)-1][len(res[0])-1]
        
obstacleGrid=[
                [0,0,0],
                [0,1,0],
                [0,0,0]
             ]
a=Solution()
print a.uniquePathsWithObstacles(obstacleGrid)