class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        k=len(costs[0])
        pre = costs[0][:]
        cur = [0]*k
        for i in xrange(1,len(costs)):
            for j in xrange(k):
                cur[j]=min([a for x,a in enumerate(pre) if x!=j])+costs[i][j]
            pre[:] = cur[:]
        return min(pre)
        