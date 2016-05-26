class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mp={}
        for i in range(26): mp[i]=chr(ord('A')+i)
        res=''
        while n>0:
            res=mp[(n-1)%26]+res # higher digit is the actual higher digit-1, 
                                 # given the above map
            n=(n-1)/26
        return res
        
    def convertToTitle2(self, n): #without map, no extra memory
        res = ''
        while n>0:
            m=(n-1)%26
            res = chr(ord('A')+m)+res
            n=(n-1)/26
        return res

a=Solution()
#print a.convertToTitle(28) #AB
#print a.convertToTitle(26) #Z
print a.convertToTitle(728) #AAZ