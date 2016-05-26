class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [(x>>1)^x for x in range(1<<n)]
        
    def grayCode2(self,n):
        res=[0]
        for i in range(n):
            highest=1<<i
            for i in range(len(res)-1,-1,-1):
                res.append(highest+res[i])
        return res
        
a=Solution()
print a.grayCode2(4)
res=a.grayCode2(4)
for a in res: print bin(a)[2:].rjust(4,"0")