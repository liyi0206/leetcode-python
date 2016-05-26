# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals=sorted(intervals,key=lambda x:x.start)
        for i in range(len(intervals)-1):
            if intervals[i+1].start<intervals[i].end:
                return False
        return True
        
a=Solution()
print a.canAttendMeetings([Interval(0,30),Interval(5,10),Interval(15,20)]) #False
print a.canAttendMeetings([Interval(7,10),Interval(2,4)]) #True