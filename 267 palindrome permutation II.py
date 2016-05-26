class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #1, res be set first, as dup exists
        #2, convert mp to list, with dups 
        
        mp={}
        for c in s:
            if c not in mp: mp[c]=1
            else: mp[c]+=1
        odd=0
        for k in mp:
            if mp[k]%2==1: odd+=1
            if odd==2: return []
        
        self.res=set()
        chars=[]
        for k in mp: chars.extend([k]*(mp[k]/2))
        
        if odd==0: self.bt(chars,"")
        else: 
            k=[k for k in mp if mp[k]%2==1][0]
            self.bt(chars,k)
        return list(self.res)
        
    def bt(self,chars,tmp):
        if not chars: 
            self.res.add(tmp)
            return
        for i,k in enumerate(chars):
            self.bt(chars[:i]+chars[i+1:],k+tmp+k)
            
a=Solution()
print a.generatePalindromes("aabb")
print a.generatePalindromes("abc")
print a.generatePalindromes("aaa")
print a.generatePalindromes("a")
print a.generatePalindromes("aaaaaa")
