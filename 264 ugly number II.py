class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q =[1]
        i2=i3=i5=0
        while len(q) < n:
            m2,m3,m5 = q[i2]*2, q[i3]*3, q[i5]*5
            m = min(m2,m3,m5) #could use heapq to make it faster
            if m==m2: i2+=1
            if m==m3: i3+=1
            if m==m5: i5+=1
            q+=[m]
        return q[-1]
        
a=Solution()
print a.nthUglyNumber(10) #12
print a.nthUglyNumber(11) #15