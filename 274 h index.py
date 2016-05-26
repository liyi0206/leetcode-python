class Solution(object):
    def hIndex(self, citations): #o(nlogn)
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]<i+1: return i
        return len(citations)
        
    def hIndex2(self, citations): #o(n) - bucket sort idea, at most n buckets
        n=len(citations)
        cnt=[0]*(n+1)
        for c in citations:
            if c<n: cnt[c]+=1
            else: cnt[n]+=1
        cntsum=0
        for i in range(n,-1,-1):
            cntsum+=cnt[i]
            if i<=cntsum: return i

a=Solution()
print a.hIndex2([3, 0, 6, 1, 5]) #3
print a.hIndex2([100]) #1
print a.hIndex2([]) #0
print a.hIndex2([0,0,0]) #0
print a.hIndex2([1,1]) #1