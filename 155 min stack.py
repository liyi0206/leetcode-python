class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.stack==[] or x <= self.minStack[-1]:
            self.minStack.append(x)
        self.stack.append(x)
        print self.stack,self.minStack

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            if self.minStack[-1] == self.stack[-1]: 
                self.minStack.pop()
            self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

print "case1"
a=MinStack()
a.push(2147483646)
a.push(2147483646)
a.push(2147483647)
print a.top()
a.pop()
print a.getMin()
a.pop()
print a.getMin()
a.pop()
a.push(2147483647)
print a.top()
print a.getMin()
a.push(-2147483648)
print a.top()
print a.getMin()
a.pop()
print a.getMin()

print "case2"
a=MinStack()
a.push(-2)
a.push(0)
a.push(-1)
print a.getMin()
print a.top()
a.pop()
print a.getMin()