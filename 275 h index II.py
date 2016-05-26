class Solution(object):
    def hIndex(self, citations): #O(logn)
        """
        :type citations: List[int]
        :rtype: int
        """
        n=len(citations)
        l,h=0,n-1
        while l<=h:
            m=l+(h-l)/2
            # if equal just return n-m. if move right, n-m smaller, not optimal;
            # if move left, citations[m-1]<=n-m, while n-m+1>n-m, still n-m.
            if citations[m]==n-m: return n-m
            elif citations[m]<n-m: l=m+1
            else: h=m-1
        # at last if no exact match, l will little exceed h, 
        # meaning n-h larger than res, n-l smaller than res. return n-l
        return n-l

a=Solution()
print a.hIndex(sorted([3, 0, 6, 1, 5])) #3