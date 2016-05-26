class Solution(object):
    def palindromePairs(self, words): #TLE #hash table, o()??
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if len(words)<2: return []
        mp={}
        for i,word in enumerate(words): mp[word]=i #words are distinct, o(n)
        
        res=set() #use set as there are dup cases 
                  # when word is "abcd" we find "abcd"+"dcba" and dcba"+"abcd", and
                  # when word is "dcba" we find again "dcba"+"abcd" and "abcd"+"dcba"
        for i,word in enumerate(words): #o(n* 2k), k is avg word length ? but Trie o(n*k^2)??
            for j in range(len(word)+1): #remember to consider k+1
                str1=word[:j]
                str2=word[j:]
                if self.isPalindrome(str1): # could be rv2+str1+str2
                    rv2=str2[::-1]
                    if rv2 in mp and mp[rv2]!=i: res.add((mp[rv2],i))
                    # mp[rv2]!=i when word is symmetric itself, and there is 
                    # no more such word to concat
                if self.isPalindrome(str2): # could be str1+str2+rv1
                    rv1=str1[::-1]
                    if rv1 in mp and mp[rv1]!=i: res.add((i,mp[rv1]))
        return list(res)
        
    def isPalindrome(self,word):
        n=len(word)
        for i in range(n/2):
            if word[i]!=word[n-i-1]: return False
        return True
        
        
a=Solution()
print a.palindromePairs(["bat","tab","cat"]) #[[0,1],[1,0]]
print a.palindromePairs(["abcd","dcba","lls","s","sssll"]) #[[0,1],[1 0],[3,2],[2,4]]
print a.palindromePairs(["a",""]) #[[0,1],[1,0]]