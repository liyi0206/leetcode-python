class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,h=0,x
        while l<=h:
            m=l+(h-l)/2
            tmp=m*m
            if tmp==x: return m
            elif tmp<x: l=m+1
            else: h=m-1
        return h
        
## edge case: x==0, x==1
"""
eg3, 0
0,0,0->return 0

eg4, 1
0,0,1->1,1,1->return 1

eg5, 9
0,4,9->0,1,3->2,2,3->3,3,3->return 3

eg6, 10
0,5,10->0,2,4->3,3,4->4,4,4->4,x,3
return 3

eg1, 12
0,6,12->0,2,5->3,4,5->3,3,3->4,x,3
return 3

eg2, 15
0,7,15->0,3,6->4,5,6->4,4,4->4,x,3
return 3

"""