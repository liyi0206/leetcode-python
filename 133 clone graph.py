# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label=x # uniquely defined lable
        self.neighbors=[]

    # need a map for {cloned node label: cloned node}
    # only for checking whether node is visited. no neighbor info
        
class Solution(object): #DFS
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        self.mp={} 
        if node == None: return None
        return self.dfs(node)

    def dfs(self,node):
        if node.label in self.mp: return self.mp[node.label]
        clone = UndirectedGraphNode(node.label)
        # once created a node, add to map, then fill neighbors
        self.mp[clone.label]=clone 
        for nb in node.neighbors: clone.neighbors.append(self.dfs(nb))
        return clone

class Solution2(object): #BFS
    def cloneGraph(self, node):
        if not node: return None
        new=UndirectedGraphNode(node.label)
        mp={new.label:new}
        cur=[node]
        while cur:
            nxt=[]
            for node in cur:
                for nb in node.neighbors:
                    if nb.label not in mp:
                        nb_clone=UndirectedGraphNode(nb.label)
                        mp[nb.label]=nb_clone
                        # nb_clone must be in mp first, then nb add to nxt
                        nxt.append(nb) 
                    mp[node.label].neighbors.append(mp[nb.label])
            cur=nxt
        return new

#node0=UndirectedGraphNode(0)
#node1=UndirectedGraphNode(1)
#node2=UndirectedGraphNode(2)
#node0.neighbors=[node1,node2]
#node1.neighbors=[node2]
#node2.neighbors=[node2]

# Must have repeated/complete neighbors
node0=UndirectedGraphNode(0)
node1=UndirectedGraphNode(1)
node2=UndirectedGraphNode(2)
node0.neighbors=[node2]
node1.neighbors=[node2]
node2.neighbors=[node0,node1]

a=Solution2()
new=a.cloneGraph(node0)
print new.label
for n in new.neighbors:
    print "new's neighbor:",n.label
    for m in n.neighbors:
        print n.label,"'s neighbor:",m.label