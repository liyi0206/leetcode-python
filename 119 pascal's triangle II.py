class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev=[1]
        for i in range(1,rowIndex+1):
            cur=[]
            for j in range(len(prev)+1):
                if j==0 or j==len(prev): cur.append(1)
                else: cur.append(prev[j-1]+prev[j])
            prev=cur
            #print cur
        return prev
        
a=Solution()
print a.getRow(5)
print a.getRow(0)