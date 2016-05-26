class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0: return []
        res = [[1]]
        for i in range(1,numRows):
            tmp=[]
            for j in range(len(res[i-1])+1):
                if j==0 or j==len(res[i-1]): tmp.append(1)
                else: tmp.append(res[i-1][j-1]+res[i-1][j])
            #print tmp
            res.append(tmp)
        return res
        
a=Solution()
print a.generate(5)