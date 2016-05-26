import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mp={}
        for n in nums:
            if n not in mp: mp[n]=1
            else: mp[n]+=1
        pq=[]
        for key in mp: heapq.heappush(pq,(-mp[key],key)) # to pop the largest
        res=[]
        for i in range(k):
            if pq: res.append(heapq.heappop(pq)[1])
        return res
        
a=Solution()
#print a.topKFrequent([1,1,1,2,2,3],2)
print a.topKFrequent([5,5,5,2,2,3],2)