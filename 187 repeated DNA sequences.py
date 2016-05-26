class Solution(object):
    def findRepeatedDnaSequences(self, s): #o(10n)
        """
        :type s: str
        :rtype: List[str]
        """
        set1=set()
        res =set()
        for i in range(len(s)-9):
            #the hashing process for s[i:i+10] is o(10)
            if s[i:i+10] not in set1: 
                set1.add(s[i:i+10])
            else: res.add(s[i:i+10])
        return list(res)
        
    def findRepeatedDnaSequences2(self, s): #o(n) - bit manipulation + robin karp
        res=[]
        val_cnt={}
        mp={'A':0,'C':1,'G':2,'T':3} 
        # num_bits = log2(len(mp))=2, so only 2 bits needed for each char
        # let n=10 DNA sequence length, n*num_bits=20 so need mask ((1<<20)-1)
        sm=0
        for x in range(len(s)):
            sm=(sm*4+mp[s[x]])&lo((1<<20)-1) #or use 0xFFFFF, in hex, F==1111
            if x<9: continue
            val_cnt[sm]=val_cnt.get(sm,0)+1
            if val_cnt[sm]==2: res.append(s[x-9:x+1])
        return res
        
a=Solution()
print a.findRepeatedDnaSequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")