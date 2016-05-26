class Solution(object):
    def canCompleteCircuit(self, gas, cost): #gauranteed only one valid
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start,sums = 0,0
        for x in range(len(gas)):
            sums += gas[x]-cost[x]
            if sums<0: start,sums = x+1,0
        return start if sum(gas)>=sum(cost) else -1

        
a=Solution()
print a.canCompleteCircuit([1,2,3,4],[4,3,2,1])
print a.canCompleteCircuit([1,2,3,3],[4,3,2,1])
print a.canCompleteCircuit([5,2,3,4],[4,3,2,1]) #several valid stations