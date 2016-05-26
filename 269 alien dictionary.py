class Solution(object):
    def alienOrder(self,words):
        """
        :type words: list[str]
        :rtype: str
        """
        if len(set(words))==1: return words[0]
        st=set()
        for word in words:
            for c in word: st.add(c) 
        #print st
        mp ={x:set() for x in st}
        mp2={x:set() for x in st}
        for i in range(len(words)-1):
            j=0
            while words[i+1][j]==words[i][j] and \
                  j<min(len(words[i]),len(words[i+1]))-1: j+=1
            mp[words[i+1][j]].add(words[i][j])
            mp2[words[i][j]].add(words[i+1][j])
        #print mp
        #print mp2
        
        cur=[x for x in mp if not mp[x]]
        res=""
        while cur:
            nxt=[]
            for x in cur:
                res+=x
                st.remove(x)
                for y in mp2[x]:
                    mp[y].remove(x)
                    if not mp[y]: nxt.append(y)
            cur=nxt
        return res if not st else ""
        
a=Solution()
print a.alienOrder(["wrt","wrf","er","ett","rftt"]) #"wertf"
print a.alienOrder(["za","zb","ca","cb"]) #zcab
print a.alienOrder([])
print a.alienOrder(["z","z"]) #z