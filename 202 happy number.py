class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = set()
        while n>1:
            a = sum([int(l)**2 for l in str(n)])
            #print a
            if a not in tmp: tmp.add(a)
            else: return False
            n = a
        return True
            
sol = Solution()
print sol.isHappy(29)