# -*- coding: utf-8 -*-
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        #if len(x)<4: return False
        #if x[2]<=x[0] and x[3]>=x[1]: return True
        #else: return False
        
        # Categorize the self-crossing scenarios, there are 3 of them: 
        # 1. 4th line crosses 1st line, 5th line crosses 2nd line, and so on
        # 2. 5th line meets 1st line, and so on
        # 3. 6th line crosses 1st line, and so on
        if len(x)<4: return False
        for i in range(3,len(x)):
            if x[i]>=x[i-2] and x[i-1]<=x[i-3]: return True
            if i>=4:
                if x[i-1]==x[i-3] and x[i]+x[i-4]>=x[i-2]: return True
            if i>=5:
                #if x[i-2]>=x[i-4] and \
                #   x[i]+x[i-4]>=x[i-2] and \
                #   x[i-1]+x[i-5]>=x[i-3] and \
                #   x[i-1]<=x[i-3]: return True
                if 0<=x[i-5]-x[i-3]+x[i-1]<=x[i-5] and \
                   0<=x[i-4]-x[i-2]+x[i]<=x[i]: return True
        return False
        
a=Solution()
print a.isSelfCrossing([1,1,2,1,1]) #True