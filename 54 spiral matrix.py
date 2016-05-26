class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m,n=len(matrix),len(matrix[0])
        if m==1: return matrix[0]
        if n==1: return [a[0] for a in matrix]

        res=[0 for i in range(m*n)]
        count=0
        for k in range((min(m,n)+1)/2):
            if k==n-k-1:
                res[count:]=[row[k] for row in matrix[k:m-k]]
            elif k==m-k-1:
                res[count:]=matrix[k][k:n-k]
            else:
                for i in range(k,n-k-1):
                    res[count]=matrix[k][i]
                    count+=1
                for j in range(k,m-k-1):
                    res[count]=matrix[j][n-k-1]
                    count+=1
                for i in range(n-k-1,k,-1):
                    res[count]=matrix[m-k-1][i]
                    count+=1
                for j in range(m-k-1,k,-1):
                    res[count]=matrix[j][k]
                    count+=1
        return res

class Solution1(object): # 4P, more concise version
    def spiralOrder(self, matrix):        
        res=[]
        if not matrix: return res
        r1,r2,c1,c2=0,len(matrix)-1,0,len(matrix[0])-1
        while r1<=r2 and c1<=c2:
            for j in range(c1,c2+1): res.append(matrix[r1][j])
            r1+=1
            for i in range(r1,r2+1): res.append(matrix[i][c2])
            c2-=1
            if r1<=r2:
                for j in range(c2,c1-1,-1): res.append(matrix[r2][j])
            r2-=1
            if c1<=c2:
                for i in range(r2,r1-1,-1): res.append(matrix[i][c1])
            c1+=1
        return res
        
        
class Solution2(object): #if matrix is mutable
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res