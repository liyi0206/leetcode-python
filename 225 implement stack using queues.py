class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.queue)-1):
            tmp = self.queue.pop(0)
            self.queue.append(tmp)
        return self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        
a=Stack()
a.push(1)
a.push(2)
print a.top()