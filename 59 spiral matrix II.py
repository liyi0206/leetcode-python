class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        count=1
        for k in range((n+1)/2):
            if k==n-k-1:
                res[k][k]=count
            else:
                for i in range(k,n-k-1):
                    res[k][i]=count
                    count+=1
                for j in range(k,n-k-1):
                    res[j][n-k-1]=count
                    count+=1
                for i in range(n-k-1,k,-1):
                    res[n-k-1][i]=count
                    count+=1
                for j in range(n-k-1,k,-1):
                    res[j][k]=count
                    count+=1
        #print res
        return res
            
        