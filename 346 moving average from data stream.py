from collections import deque
class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size=size
        self.queue=deque([])
        self.sum=0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue)<self.size: 
            self.queue.append(val)
            self.sum+=val
            return float(self.sum)/len(self.queue)
        else:
            old=self.queue.popleft()
            self.sum-=old
            self.queue.append(val)
            self.sum+=val
            return float(self.sum)/self.size

m = MovingAverage(3);
print m.next(1) #= 1
print m.next(10)#= (1 + 10) / 2
print m.next(3) #= (1 + 10 + 3) / 3
print m.next(5) #= (10 + 3 + 5) / 3