class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1=(C-A)*(D-B)
        area2=(G-E)*(H-F)
        w = max(min(C,G)-max(A,E),0)
        h = max(min(D,H)-max(B,F),0)
        intersection=w*h
        return area1+area2-intersection
        
a=Solution()
print a.computeArea(-3,0,3,4,0,-1,9,2) #45