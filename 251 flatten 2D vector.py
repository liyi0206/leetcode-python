class Vector2D(object): #using index ********
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vecs=vec2d # only reference, o(1) space
        self.x=0
        self.y=0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            res=self.vecs[self.x][self.y]
            self.y+=1 # prep for next
            return res
        else: return None

    def hasNext(self): #update x,y, and return T/F
        """
        :rtype: bool
        """
        while self.x<len(self.vecs) and self.y==len(self.vecs[self.x]):
            self.x+=1
            self.y =0
        return self.x<len(self.vecs)
        
class Vector2D2(object): # using iter, assumably
    def __init__(self, vec2d): 
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vecs = vec2d #iter([iter(v) for v in vec2d])
        
    def next(self):
        if self.hasNext():
            top = self.vecs[0] #next()
            res = top.pop(0) #pop(0) o(n) time, next o(1) time
            if not top: self.vecs.pop(0) #pop(0) o(n) time, next o(1) time
            return res
        else: return None

    def hasNext(self):
        return self.vecs!=[]
        
vec2d=[[1,2], [3], [4,5,6]]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
print v