class Solution(object):
    # save all rows (n*n)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        g = [[0] * n for i in range(m)]
        for i in range(m): g[i][0] = 1
        for j in range(n): g[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] = g[i][j-1] + g[i-1][j]
        return g[m-1][n-1]
        
    # save only two rows (2*n)
    #def uniquePaths(self, m, n):        
    #    dp0 = [1]*n
    #    dp1 = [1]+[0]*(n-1)
    #    for i in range(1, m):
    #        for j in range(1, n):
    #            dp1[j] = dp1[j-1] + dp0[j]
    #        dp0 = dp1
    #        dp1[0]=1
    #        #dp1 = [1]+[0]*(n-1)
    #    return dp0[-1]
        
a=Solution()
print a.uniquePaths(3,3)