class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1, 1]
        while len(f) <= n:
            f.append(f[-1] + f[-2])
        return f[n]