class Solution(object):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    def findOrder1(self,numCourses,prerequisites): #BFS best version
        mp1={x:[] for x in range(numCourses)}
        mp2={x:[] for x in range(numCourses)}
        for c1,c2 in prerequisites: 
            mp1[c1].append(c2) #prereqs
            mp2[c2].append(c1) #dependents
        #print mp1,mp2
        cur=[x for x in mp1 if mp1[x]==[]]
        res=[]
        while cur and numCourses>0:
            res+=cur
            numCourses-=len(cur)
            next=[]
            for x in cur:
                for y in mp2[x]:
                    mp1[y].remove(x)
                    if mp1[y]==[]:next.append(y)
            cur=next
        return res if numCourses == 0 else []

    def findOrder2(self, numCourses, prerequisites): #DFS best version
        self.mp = {x:[] for x in range(numCourses)} #prereqs
        self.mark={x:0  for x in range(numCourses)}
        for a0,a1 in prerequisites: self.mp[a0].append(a1)
       
        self.res=[]
        self.valid=True
        for x in range(numCourses): self.dfs(x)
        return self.res if self.valid else []

    def dfs(self,v):
        if self.mark[v]==1: return
        if self.mark[v]==2: 
            self.valid=False
            return
        
        self.mark[v] = 2
        if self.mp[v]:
            for p in self.mp[v]: self.dfs(p)
        self.mark[v] = 1
        self.res.append(v)

a=Solution()
print a.findOrder2(4, [[1,0],[2,0],[3,1],[3,2]]) #[0,1,2,3] or [0,2,1,3]
print a.findOrder2(2, [[1,0],[0,1]]) #[]