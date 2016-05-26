class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mp =  {1: "I", 
               4: "IV", 5: "V", 
               9: "IX", 10: "X", 
               40: "XL", 50: "L", 
               90: "XC", 100: "C", 
               400: "CD", 500: "D", 
               900: "CM", 1000: "M"}
        keys = sorted(mp.keys(),reverse=True)
        res=""
        for k in keys:
            while num/k > 0:
                res += mp[k]
                num -= k
        return res
        
a=Solution()
print a.intToRoman(6789)