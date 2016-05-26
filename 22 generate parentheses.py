class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.bt(n,n,"")
        return self.res
        
    def bt(self,left,right,tmp):
        if left == 0 and right == 0: 
            self.res.append(tmp)
        if left > 0:
            self.bt(left-1,right,tmp+"(")
        if left < right:
            self.bt(left,right-1,tmp+")")
        
    # logging version
    #def bt(self,left,right,tmp):
    #    #print "in bt. left,right,tmp:",left,right,tmp
    #    if left == 0 and right == 0: 
    #        self.res.append(tmp)
    #        print "finish everything",self.res
    #    if left > 0:
    #        print "start from left. left,right,tmp",left,right,tmp,
    #        print "---> left,right,tmp",left-1,right,tmp+"("
    #        self.bt(left-1,right,tmp+"(")
    #        print "done with left. left,right,tmp:",left,right,tmp,"\n"
    #    if left < right:
    #        print "start from right. left,right,tmp",left,right,tmp,
    #        print "---> left,right,tmp",left,right-1,tmp+")"
    #        self.bt(left,right-1,tmp+")")
    #        print "done with right. left,right,tmp:",left,right,tmp          


a=Solution()
print a.generateParenthesis(3)