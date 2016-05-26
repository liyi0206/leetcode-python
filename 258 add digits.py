class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #while len(str(num))>1:
        #    num=sum([int(a) for a in str(num)])
        #return num
        
        while num>9:
            tmp=0
            while num:
                tmp+=num%10
                num=num/10
            num=tmp
        return num
        
a=Solution()
print a.addDigits(38)