class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        p1,p2 = 0,len(h)-1
        while p1<=p2:
            print p1,p2,min(h[p1],h[p2])*(p2-p1)
            res = max(res, min(h[p1],h[p2])*(p2-p1))
            if h[p1] < h[p2]: p1=p1+1
            else: p2=p2-1
        return res
        
    def maxArea2(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        p1,p2 = 0,len(h)-1
        while p1<=p2:
            print p1,p2,min(h[p1],h[p2])*(p2-p1)
            res = max(res, min(h[p1],h[p2])*(p2-p1))
            if h[p1] < h[p2]: 
                t=p1
                p1=p1+1
                while h[p1]<=h[t] and p1<=p2:
                    p1=p1+1
            else: 
                s=p2
                p2=p2-1
                while h[p2]<=h[s] and p1<=p2:
                    p2=p2-1
        return res
            
a = Solution()
print a.maxArea2([1,2,4,3]) #4