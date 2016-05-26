class Solution(object):
    def countComponents(self,n,edges): #union find
        roots=range(n)
        res=n
        for n1,n2 in edges:
            x=self.find(roots,n1) 
            y=self.find(roots,n2)
            if x!=y:
                roots[y]=x # union - no comparison for who's father
                res-=1
        return res
        
    def find(self,roots,id):
        while roots[id]!=id:
            # self.roots or reference roots are same - python takes pointer
            roots[id]=roots[roots[id]] # for flatten tree
            id=roots[id] # for find the root
        return id

a=Solution()
print a.countComponents(5,[[0,1],[1,2],[3,4]]) #2
print a.countComponents(5,[[0,1],[1,2],[2,3],[3,4]]) #1
print a.countComponents(4,[[0,1],[0,2],[1,2]]) #2

class Solution2(object):
    def countComponents2(self,n,edges): #dfs
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n==0: return 0
        self.nodes=set(range(n))
        #dict(zip(range(n),[[]]*n)) won't work, all keys move together
        self.mp={node:[] for node in range(n)}
        for node1,node2 in edges:
            self.mp[node1].append(node2)
            self.mp[node2].append(node1)
        
        res=0
        for i in range(n):
            if i in self.nodes: #also needed, to control res increments
                self.dfs(i)
                res+=1
                #print self.nodes
        return res
        
    def dfs(self,i):
        #needed as we may come to the visited nodes of the current cycle
        if i not in self.nodes: return 
        self.nodes.remove(i)
        for neighbor in self.mp[i]:
            self.dfs(neighbor)