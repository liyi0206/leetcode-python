# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals): #dont' understand, o(n)
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        e = 0
        numRooms,available = 0,0
        for start in starts:
            while ends[e] <= start:
                available += 1
                e += 1
            if available: available -= 1
            else: numRooms += 1
        return numRooms
        
    def minMeetingRooms1(self,intervals): #most straight forward, o(n)
        if not intervals: return 0

        times=[]
        for n in range(len(intervals)):
            times.append(intervals[n].start)
            times.append(-intervals[n].end)
        times.sort() #stability of sort
        times.sort(key=lambda x:abs(x))
        
        res,cur = 0,0
        for x in times:
            if x>=0: cur+=1
            else: cur-=1
            res = max(cur,res)
        return res
        
    def minMeetingRooms2(self,intervals): #min heap, o(nlogn)
        if not intervals: return 0
        intervals=sorted(intervals,key=lambda x:x.start)
        import heapq
        heap=[(intervals[0].end, intervals[0])]
        for i in range(1,len(intervals)):
            end,interval=heapq.heappop(heap)
            if intervals[i].start>=end:
                heapq.heappush(heap,(intervals[i].end,intervals[i]))
            else:
                heapq.heappush(heap,(intervals[i].end,intervals[i]))
                heapq.heappush(heap,(interval.end,interval))
        return len(heap)
        
a=Solution()
print a.minMeetingRooms1([Interval(0,30),Interval(5,10),Interval(15,20)]) #2
