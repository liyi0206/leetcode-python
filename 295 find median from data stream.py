class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxHeap,self.minHeap=[],[]
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        import heapq #heapq has min at [0] or pop()
        minTop =-self.minHeap[0] if len(self.minHeap) else None
        maxTop = self.maxHeap[0] if len(self.maxHeap) else None
        minSize,maxSize = len(self.minHeap),len(self.maxHeap)
        if maxSize==0 or minSize==0:
            if maxSize==minSize==0: heapq.heappush(self.maxHeap,num)
            elif minSize==0 and num>maxTop: 
                heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap,num)
                heapq.heappush(self.minHeap,-maxTop)
            elif minSize==0:
                heapq.heappush(self.minHeap,-num)
        else:
            if num>maxTop:
                heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap,num)
                num=maxTop
            elif num<minTop:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap,-num)
                num = minTop
            if minSize<maxSize: heapq.heappush(self.minHeap,-num) #so first max if equal
            else: heapq.heappush(self.maxHeap,num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minHeap)<len(self.maxHeap):
            return float(self.maxHeap[0])
        else:
            return float(-self.minHeap[0]+self.maxHeap[0])/2
            
from heapq import *
class MedianFinder2:     # python heapq pop smallest, 
    def __init__(self):  # but here small heap need to pop largest
        self.heaps=[],[] # python heapq peek - [0] (other idx not tell size)

    def addNum(self, num): 
        small,large = self.heaps
        heappush(small, -heappushpop(large,num))
        if len(large)<len(small): heappush(large,-heappop(small))

    def findMedian(self):
        small,large = self.heaps
        if len(large)>len(small): return float(large[0])
        return (large[0]-small[0])/2.0

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2);print mf.maxHeap,mf.minHeap
print mf.findMedian() #1.5
mf.addNum(3);print mf.maxHeap,mf.minHeap
print mf.findMedian() #2

mf = MedianFinder()
mf.addNum(-1);print mf.maxHeap,mf.minHeap
print mf.findMedian()
mf.addNum(-2);print mf.maxHeap,mf.minHeap
print mf.findMedian()
mf.addNum(-3);print mf.maxHeap,mf.minHeap
print mf.findMedian()
mf.addNum(-4);print mf.maxHeap,mf.minHeap
print mf.findMedian()
mf.addNum(-5);print mf.maxHeap,mf.minHeap
print mf.findMedian() #3

mf = MedianFinder()
mf.addNum(2);print mf.maxHeap,mf.minHeap
print mf.findMedian()
mf.addNum(3);print mf.maxHeap,mf.minHeap
print mf.findMedian()