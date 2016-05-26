class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.bt(4,s,"")
        return self.res

    def bt(self, num, s, tmp): #num is num_unpopulated_segments
        if num*3 < len(s): return  #pruning
        if num == 1:               #last one piece of s
            if self.is_valid(s):
                self.res.append(tmp+s)
        else:
            for i in range(1,4):
                if len(s) > i and self.is_valid(s[:i]):
                    self.bt(num-1,s[i:],tmp+s[:i]+'.')
                
    def is_valid(self, s):
        if s[0] == "0" and s != "0": return False
        return int(s) < 256
        
a=Solution()
print a.restoreIpAddresses("25525511135")