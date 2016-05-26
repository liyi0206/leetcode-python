# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class IteratorWrapper(object):
    def __init__(self, it):
        self.it = iter(it)
        self._hasnext = None
        self._thenext = None
    def __iter__(self): return self
    def next(self):
        if self._hasnext: res = self._thenext
        else: res= next(self.it)
        self._hasnext = None
        return res
    def hasNext(self):
        if self._hasnext is None:
            try: self._thenext = next(self.it)
            except StopIteration: self._hasnext = False
            else: self._hasnext = True
        return self._hasnext
        
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter=iterator
        self.nxt=None 
        if self.iter.hasNext(): self.nxt=self.iter.next()

    def hasNext(self):
        return self.nxt is not None

    def peek(self):
        return self.nxt

    def next(self): # the actual step is still taken in next()
        res=self.nxt
        self.nxt=self.iter.next() if self.iter.hasNext() else None
        return res
 
i=PeekingIterator(IteratorWrapper([1,2,3,4,5,6]))
while i.hasNext(): 
    print "peek",i.peek(),
    print "next",i.next()
