# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head): # mp is {old_node: new_node}
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        new=RandomListNode(head.label)
        mp={new.label:new}
        p1,p2=head,new
        while p1:
            nxt=p1.next
            if nxt and nxt not in mp:
                mp[nxt]=RandomListNode(nxt.label)
            p2.next=mp[nxt] if nxt else None
            
            rdm=p1.random
            if rdm and rdm not in mp:
                mp[rdm]=RandomListNode(rdm.label)
            p2.random=mp[rdm] if rdm else None
            
            p1,p2=nxt,p2.next
        return new
        
    def copyRandomList2(self, head): # mp is {label: new_node}
        if not head: return None
        new=RandomListNode(head.label)
        mp={new.label:new}
        p1,p2=head,new
        while p1:
            nxt=p1.next
            if nxt and nxt.label not in mp:
                mp[nxt.label]=RandomListNode(nxt.label)
            p2.next=mp[nxt.label] if nxt else None
            
            rdm=p1.random
            if rdm and rdm.label not in mp:
                mp[rdm.label]=RandomListNode(rdm.label)
            p2.random=mp[rdm.label] if rdm else None
            
            p1,p2=nxt,p2.next
        return new
        
node1,node2,node3 = RandomListNode(1),RandomListNode(2),RandomListNode(3)
node1.next = node2; node1.random = node3
node2.next = node3; node2.random = node1
node3.random = node2

a=Solution()
copy = a.copyRandomList(node1)
print copy.label
print copy.next.label
print copy.random.label