class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1: return s
        res=[[] for a in range(numRows)]
        j,flag=0,1
        for i in range(len(s)):
            res[j].append(s[i])
            if j==numRows-1: flag=-1
            if j==0: flag=1
            j+=flag       
        #print res
        return ''.join([''.join(a) for a in res])
        
a=Solution()
print a.convert("PAYPALISHIRING",3)
print a.convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ",5)
print a.convert("AB",1)