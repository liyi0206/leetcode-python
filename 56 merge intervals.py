# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return intervals
        intervals.sort(key = lambda x: x.start)
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end: 
                res[-1].end = max(res[-1].end, intervals[i].end)
            else: res.append(intervals[i])
        return res
  
int1=Interval(1,3)
int2=Interval(2,6)  
int3=Interval(8,10)
int4=Interval(15,18)   
intervals=[int1,int2,int3,int4]
a=Solution()
res=a.merge(intervals)
for a in res:
    print a.start,a.end