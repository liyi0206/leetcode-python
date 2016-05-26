class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.mp={}
        self.queue=[]

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.mp:
            self.queue.remove(key)
            self.queue.append(key)
            return self.mp[key]
        else: return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.mp:
            self.queue.remove(key)
            self.queue.append(key)
            self.mp[key]=value
        else:
            if len(self.queue) == self.cap:
                old_key=self.queue.pop(0)
                self.mp.pop(old_key,None)
            self.queue.append(key)
            self.mp[key]=value

#1,GET - update queue, return mp value
#2,SET - if in, update queue, update mp value;
#        if not in, delete old key per cap, add to queue and mp
### mp is the actual place to save values

print "case1"   
a=LRUCache(1)
a.set(2,1)
print a.get(2)

print "case2"
a=LRUCache(1)
a.set(2,1)
print a.get(2)
a.set(3,2)
print a.get(2)
print a.get(3)

print "case3"
a=LRUCache(2)
print a.get(2)
a.set(2,6)
print a.get(1)
a.set(1,5)
a.set(1,2)
print a.get(1)
print a.get(2)

# double linked list is the correct solution, 
# because removing elem from array is o(n)
## DBLL is the actual place to save values

# the reason is - in array queue, we could find value by idx (queue.remove(key))
# but in DBLL, we need a map to find node by key, so the value of map must be node
# thus the actual value need to be stored in DBLL.

class DLNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
         
class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head,self.tail = DLNode(0,0),DLNode(0,0) #dummies
        self.head.next = self.tail #
        self.tail.pre = self.head #
     
    # key point is to keep head and tail as dummies
    # when remove an add, operate pre/nxt at the same time
    
    def rmNode(self,node):  ###
        pre,nxt = node.pre,node.next
        pre.next,nxt.pre = nxt,pre
     
    def addTail(self,node):  ###
        pre = self.tail.pre
        pre.next,node.pre = node,pre
        node.next,self.tail.pre = self.tail,node
 
    def get(self, key):
        if key in self.map:
            self.rmNode(self.map[key])
            self.addTail(self.map[key])
            return self.map[key].val            
        else: return -1
 
    def set(self, key, value):
        if key in self.map:
            self.rmNode(self.map[key])
            self.addTail(self.map[key])
            self.map[key].val = value
        else:
            if len(self.map)==self.cap:
                old_node = self.head.next   ######
                self.rmNode(old_node)
                self.map.pop(old_node.key,None) #only place to use key in list
            node = DLNode(key,value)
            self.addTail(node)
            self.map[key] = node #node, not value