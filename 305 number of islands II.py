class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m<=0 or n<=0: return []
        res=[]
        count=0
        roots=[-1]*(m*n)
        
        for x,y in positions:
            #print (x,y)
            #0, create roots[p], count++
            p=n*x+y
            roots[p]=p # only gives root when water becomes island
            count+=1   # assume new point is isolated island
            for dx,dy in ((0,-1),(0,1),(-1,0),(1,0)):
                nx,ny=x+dx,y+dy
                np=n*nx+ny
                #1, skip invalid new positions
                if not (0<=nx<m and 0<=ny<n) or roots[np]==-1: continue
                #2, find root for new position
                root_np=self.find(roots,np)
                #3, change position's root if different, and transfer position, counter--
                #print p,root_np
                #print "pre  roots",roots
                if roots[p]!=root_np:# if neighbor is another island
                    roots[p]=root_np # union
                    p=root_np ### transfer the change power to the root
                    # when we change roots[p] to be root_np, if not change position
                    # to the root, next time we will simply change roots[p] again 
                    # to a new value, and the two parts are still not connected.
                    count-=1
                #print "post roots",roots
            res.append(count)
        return res
        
    def find(self,roots,p):
        while roots[p]!=p:
            roots[p]=roots[roots[p]] # for flatten tree
            p=roots[p] # for find the root
        return p
        
a=Solution()
#print a.numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]]) #[1,1,2,3]
print a.numIslands2(3,3,[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]) #[1,2,3,4,3,2,1]