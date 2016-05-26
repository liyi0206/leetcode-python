class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp =  {"I":1, 
               "IV":4, "V":5, 
               "IX":9, "X":10, 
               "XL":40, "L":50, 
               "XC":90, "C":100, 
               "CD":400, "D":500, 
               "CM":900, "M":1000}
        keys = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res=0
        for k in keys:
            #print k
            while s.startswith(k):
                res+=mp[k]
                s=s[len(k):]
                #print res,k,s
        return res
        
a=Solution()
print a.romanToInt("MMMMMMDCCLXXXIX")