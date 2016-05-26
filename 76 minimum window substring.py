class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mp={}
        for c in t:
            if c not in mp: mp[c]=1
            else: mp[c]+=1
            
        res=""
        counter=len(mp)
        p1,p2=0,0
        while p2<len(s):
            if s[p2] in mp:
                mp[s[p2]]-=1
                if mp[s[p2]]==0: counter-=1
                if counter==0:
                    while counter==0:
                        if s[p1] in mp:
                            mp[s[p1]]+=1
                            if mp[s[p1]]>0: counter+=1
                        p1+=1
                    if res=="" or p2-(p1-1)+1<len(res):
                        res=s[p1-1:p2+1]
            p2+=1
        return res


a=Solution()
print a.minWindow("ADOBECODEBANC", "ABC") #BANC