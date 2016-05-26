class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1=version1.split(".")
        v2=version2.split(".")
        for i in range(min(len(v1),len(v2))):
            if int(v1[i])>int(v2[i]): return 1
            elif int(v1[i])<int(v2[i]): return -1
        if len(v1)>len(v2):
            for j in range(i+1,len(v1)): 
                if int(v1[j])!=0: return 1
        elif len(v2)>len(v1):
            for j in range(i+1,len(v2)): 
                if int(v2[j])!=0: return -1
        return 0
        
a=Solution()
print a.compareVersion("0.1", "0.0.1") #1