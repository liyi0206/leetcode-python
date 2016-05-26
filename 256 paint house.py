class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # n houses, each can be painted with one of the three colors
        # costs[1][2] is the cost of painting house 1 with color 2
        
        if not costs: return 0
    
        pre = costs[0][:] #cost of paint house 0 with color 1-3
        cur = [0]*3
        for i in xrange(1,len(costs)):
            cur[0] = min(pre[1],pre[2])+costs[i][0]
            cur[1] = min(pre[0],pre[2])+costs[i][1]
            cur[2] = min(pre[0],pre[1])+costs[i][2]
            pre[:] = cur[:]
        return min(pre)