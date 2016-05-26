class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        pass
        
class Solution3(object):
    # hard point1, * has higher priority than +-
    # hard point2, number could be any digits
    def addOperators(self, num, target):
        self.res, self.target = [], target
        for i in range(1,len(num)+1):
            if i>1 and num[0]=="0": continue # prevent "00*" as a number
            self.dfs(num[i:],num[:i],int(num[:i]),int(num[:i]))
        return self.res
    
    def dfs(self, num, temp, cur, last):
        # num: remaining num string
        # temp: temporally string with operators added
        # cur:  current result of "temp" string
        # last: last multiply-level number in "temp". if next operator is 
        #       "multiply", "cur" and "last" will be updated

        if not num:
            if cur==self.target: self.res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i>1 and num[0]=="0": continue # for hard point 2
            self.dfs(num[i:], temp+"+"+val, cur+int(val), int(val))
            self.dfs(num[i:], temp+"-"+val, cur-int(val),-int(val))
            self.dfs(num[i:], temp+"*"+val, cur-last+last*int(val), last*int(val))
                                             # for hard point 1
        
a=Solution()
print a.addOperators2("123", 6)
#print a.addOperators2("232", 8)
#print a.addOperators2("105", 5)
#print a.addOperators2("00", 0)
#print a.addOperators("3456237490", 9191)