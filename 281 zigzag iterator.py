class ZigzagIterator(object):
    def __init__(self, v1, v2): # merge in init, o(n) space, using index
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.idx=-1
        self.queue=[] #o(n) space
        for i in range(max(len(v1),len(v2))):
            if i<len(v1): self.queue.append(v1[i])
            if i<len(v2): self.queue.append(v2[i])
        self.n=len(self.queue)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx+1<self.n: return True
        else: return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext: 
            self.idx+=1
            return self.queue[self.idx]
        else: return None

class ZigzagIterator1(object): #init only load, o(1) space, using index
    def __init__(self, v1, v2):
        self.N = 2
        self.M = max(len(v1),len(v2))
        self.m,self.n = 0,0
        self.v1,self.v2 = v1,v2 #only reference, o(2) space
         
    def next(self):
        if self.hasNext(): 
            n,m = self.n,self.m
            self.n = (self.n+1)%self.N # prep for next
            if self.n==0: self.m+=1    # prep for next
            return self.v1[m] if n==0 else self.v2[m]
        else: return None
 
    def hasNext(self):
        # get out of while loop, either b/c m>=M (no more, return False), 
        # or find candidate in v1 or v2 (continue, return True)
        while self.m<self.M and \
        not (self.n==0 and self.m<len(self.v1)) and \
        not (self.n==1 and self.m<len(self.v2)): 
            self.n=(self.n+1)%self.N
            if self.n==0: self.m+=1
        if self.m<self.M: return True
        else: return False
        
class ZigzagIterator2(object): # need queue for vecs, linked list for queues, 
                               # o/w time complexity is huge
    def __init__(self, v1, v2):
        # self.queue=[v1,v2], easier pattern for k vectors
        self.queue=[v for v in (v1,v2) if v]
    
    def hasNext(self):
        if self.queue: return True
        return False
    
    def next(self):
        # easy to extend to k vectors
        v=self.queue.pop(0) # assume real queue, pop(0) is o(1)
        ret=v.pop(0)
        if v: self.queue.append(v)
        return ret

#v1 = [1, 2]
#v2 = [3, 4, 5, 6]
#i, v = ZigzagIterator2(v1,v2), []
#while i.hasNext(): v.append(i.next())
#print v
        
########### consider input as iteratros, not lists/arrays ###########
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
    def hasnext(self):
        if self._hasnext is None:
            try: self._thenext = next(self.it)
            except StopIteration: self._hasnext = False
            else: self._hasnext = True
        return self._hasnext

from collections import deque
class ZigzagIterator3(object): # use deque to organize input iters
    def __init__(self,v1,v2):  # for deque implementation, popleft is o(1)
        self.queue=deque([v1,v2])  # python queue is implemented as list, pop() is o(n)
        
    def hasNext(self):
        if self.queue: return True
        else: return False
        
    def next(self):
        v=self.queue.popleft()
        ret=v.next()
        if v.hasnext(): self.queue.append(v)
        return ret

class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
class ZigzagIterator4(object): # use linked list to organize input iters
    def __init__(self,v1,v2):
        self.head=ListNode(v1)
        self.tail=ListNode(v2)
        self.head.next=self.tail
        
    def hasNext(self):
        if self.head: return True
        else: return False
        
    def next(self):
        cur=self.head
        ret=cur.val.next()
        if self.head!=self.tail:
            self.head=self.tail
            if cur.val.hasnext():
                self.head.next=cur
                self.tail=cur
        elif not cur.val.hasnext():
            self.head=None
            self.tail=None
        return ret
           
v1 = IteratorWrapper([1, 2])
v2 = IteratorWrapper([3, 4, 5, 6])
i= ZigzagIterator4(v1,v2)
while i.hasNext(): print i.next()

#a=iter([1,2,3])
#a.next();a.next();a.next()
## method1 hasnext
#if next(a,None)==None: print "empty!"
## method2 hasnext
#try: a.next()
#except StopIteration: print "empty!"
