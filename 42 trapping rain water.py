class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        maxl,maxr=[],[]
        tmp=0
        for i in range(len(height)):
            if height[i]>tmp: tmp=height[i]
            maxl.append(tmp)
        tmp=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>tmp: tmp=height[i]
            maxr.append(tmp)
        area=0
        for i in range(1,len(height)-1):
            minh=min(maxl[i],maxr[len(height)-i-1])-height[i]
            area+=minh if minh>0 else 0
        return area
        
#class Solution(object):
#    def trap(self, height):
#        area=0        
#        for i in range(1,len(height)-1):
#            lmax=max(height[:i])
#            rmax=max(height[i+1:])
#            tmin=min(lmax-height[i], rmax-height[i])
#            tmax=max(lmax-height[i], rmax-height[i])
#            if tmin>0 and tmax>0:
#                area+=tmin
#            #print i,area
#        return area
            