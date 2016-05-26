# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object): # input is list, using index
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nestedList,i = self.stack[-1]
            if i==len(nestedList): self.stack.pop()
            else:
                x =nestedList[i]
                if x.isInteger(): return True
                self.stack[-1][1]+=1 #for next round
                self.stack.append([x.getList(), 0])
        return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            nestedList,i = self.stack[-1]
            self.stack[-1][1]+=1
            return nestedList[i].getInteger()
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class DeepIterator2(): # input is list of numbers, keep stack of array and index
    def __init__(self,nestedList):
        self.stack = [[nestedList,0]] # only reference, o(1) space
    
    def hasnext(self):
        while self.stack:
            nestedList,i = self.stack[-1]
            if i==len(nestedList): 
                self.stack.pop()
                if self.stack: self.stack[-1][1]+=1
                else: return False
            else:
                x=nestedList[i]
                if type(x)==int: return True
                else: self.stack.append([x,0])
        
    def next(self):
        if not self.hasnext(): return None
        nestedList,i = self.stack[-1]
        self.stack[-1][1]+=1 # prep for next, only actual change
        return nestedList[i]
     
#nums=[1,2,[3,4,5,[],[6,7,[8,9],10]],[[]],11,12]
#di=DeepIterator2(nums)
#for i in range(12): print di.next()

### input is iterator
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
        
class DeepIterator3(): # input is list of numbers, keep stack of array and index
    def __init__(self,nestedList): # the problem with it is there is a hasnext 
        self.stack = [nestedList]  # True at last element
        
    def hasNext(self):
        if self.stack: return True
        else: return False
                
    def next(self):
        while self.stack:
            cur=self.stack[-1]
            if cur.hasnext():
                x=cur.next()
                if type(x)==int: return x
                else: self.stack.append(x)
            else: self.stack.pop()
        
nestedList = IteratorWrapper([1,2,IteratorWrapper([3,4,5,IteratorWrapper([]),
                            IteratorWrapper([6,7,IteratorWrapper([8,9]),10])]),
                            IteratorWrapper([IteratorWrapper([])]),11,12])
i = DeepIterator3(nestedList)
while i.hasNext(): print i.next()