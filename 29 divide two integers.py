class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #if dividend==-1<<31 and divisor==-1:
        #    return (1<<31)-1
        if divisor==0: return (1<<31)-1
        ans = 0
        if dividend == -1<<31:
            ans=1
            dividend+=abs(divisor)
        if divisor==-1<<31: return ans    
        flag=1 if dividend*divisor<0 else 0
        
        dividend,divisor =abs(dividend),abs(divisor)
        digit=0
        while divisor<=(dividend/2):
            divisor*=2
            digit+=1
        while digit>=0:
            if dividend>=divisor:
                dividend-=divisor
                ans+=2**digit #ans=min(ans+2**digit,(1<<31)-1)
            divisor/=2
            digit-=1
        res=ans if flag==0 else -ans
        res=min(res,(1<<31)-1)
        return res