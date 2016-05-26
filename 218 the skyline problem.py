# -*- coding: utf-8 -*-
class Solution(object):
    def getSkyline(self, buildings): #min heap, o(nlogn)
        # ****** in theory, use BST instead of PQ, for o(nlogn) time *******
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ### need 3 containers in total - 
        #1,heights - (loc1,-h) and (loc2,h) for each bldg, from buildings input
        #2,queue - for heights (start with 0 to make max(queue) always work)
        #3,res - for key points (loc, new_height); and prev (start from 0)
        
        #1, create array for (loc,height) tuples (left height negative)
        #2, sort by locs
        height=[]
        for b in buildings:
            height.append((b[0],-b[2])) #left,-height
            height.append((b[1],b[2]))  #right,height
        height.sort() # o(nlogn)
        #print height
        
        queue=[0] ## to make max(queue) no error, when in no building period
        prev=0 ## to compare with cur
        res=[]
        # for each (loc,height) -
        #1, push to queue or pop from queue
        #2, get new height (if different, append (loc,new height) to res and update prev)
        for h in height: #o(nlogn) 
            #print h
            if h[1]<0: queue.append(-h[1]) # if left point - o(logn)
            else: queue.remove(h[1]) #python heapq doesn't have remove
                                     #PQ remove o(n), as it takes o(n) to find
            #print "    queue",queue
            cur=max(queue) #new height
            if prev!=cur:
                res.append((h[0],cur)) #new left, new height
                prev=cur
            #print "    res",res
        return res
        
a=Solution()
print a.getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]])
#[[2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]]