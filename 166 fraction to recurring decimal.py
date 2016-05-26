class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator==0: return ""
        if numerator==0: return "0" #early return to avoid adding "-"
        
        res=""
        #1, sign
        if (numerator<0)^(denominator<0): res+="-"
        #2, int part
        n,d=abs(numerator),abs(denominator)
        res+=str(n/d)
        #3, fractional part - find pattern in residual
        r=n%d
        if r==0: return res
        else: res+="."
        
        mp={}
        while r:
            if r in mp: 
                res=res[:mp[r]]+"("+res[mp[r]:]+")"
                return res
            mp[r]=len(res)
            r*=10
            res+=str(r/d) # the mp[r] idx in res
            r=r%d
        return res
        
a=Solution()
#print a.fractionToDecimal(1,2)
#print a.fractionToDecimal(2,1)
#print a.fractionToDecimal(2,3)
print a.fractionToDecimal(-50,8)