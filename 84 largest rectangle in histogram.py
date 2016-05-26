# -*- coding: utf-8 -*-
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        increasing, area, i = [], 0, 0
        while i <= len(heights):
            if len(increasing)==0 or (i<len(heights) and heights[i]>heights[increasing[-1]]):
                increasing.append(i)
                i += 1
            else: #saved one layer of loop
                last = increasing.pop()
                if len(increasing) == 0: area = max(area, heights[last]*i)
                else: area = max(area, heights[last]*(i-1-increasing[-1]))
        return area
        
    def largestRectangleArea2(self, heights):
        if len(heights)==0: return 0
        res=0
        heights.append(0)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                tmp=stack.pop()
                if not stack: w=i
                else: w=i-1-stack[-1]
                res=max(res, w*heights[tmp])
            stack.append(i)
            #print i,stack
        return res
                
a=Solution()
#print a.largestRectangleArea([2,1,5,6,2,3]) #10
#print a.largestRectangleArea([1]) #1
#print a.largestRectangleArea([2,1,2]) #3
print a.largestRectangleArea([2,1,6,5,4,1,2,3,2])