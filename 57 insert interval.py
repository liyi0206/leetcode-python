# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        return self.merge(intervals + [newInterval])
        
    def merge(self, intervals):
        if len(intervals) == 0: return intervals
        intervals.sort(key = lambda x: x.start)
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end: 
                res[-1].end = max(res[-1].end, intervals[i].end)
            else: res.append(intervals[i])
        return res
   
class Solution2(object): # better
    def insert(self,intervals,newInterval):
        if not intervals: return [newInterval]
        i=0
        while i<len(intervals) and intervals[i].end<newInterval.start: i+=1
        idx=i
        mergeInterval=Interval(newInterval.start,newInterval.end)
        while i<len(intervals) and not (newInterval.end<intervals[i].start):
            mergeInterval.start=min(intervals[i].start,mergeInterval.start)
            mergeInterval.end=max(intervals[i].end,mergeInterval.end)
            i+=1
        return intervals[:idx]+[mergeInterval]+intervals[i:]
             
             
a=Solution2()
res=a.insert([Interval(1,3),Interval(6,9)], Interval(2,5))
for a in res: print a.start,a.end