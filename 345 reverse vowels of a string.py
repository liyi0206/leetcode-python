class Solution(object):
    def reverseVowels(self, s): #TLE
        """
        :type s: str
        :rtype: str
        """
        vowels=[]
        for c in s:
            if c in "aeiou":
                vowels.append(c)
        res=""
        for c in s:
            if c not in "aeiou":
                res+=c
            else:
                res+=vowels.pop()
        return res

class Solution2(object):
    def reverseVowels(self, s): #AC
        p1,p2=0,len(s)-1
        s=list(s)
        while p1<p2:
            while s[p1] not in "aeiouAEIOU" and p1<p2: p1+=1
            while s[p2] not in "aeiouAEIOU" and p1<p2: p2-=1
            if s[p1] in "aeiouAEIOU" and s[p2] in "aeiouAEIOU":
                s[p1],s[p2]=s[p2],s[p1]
                p1,p2=p1+1,p2-1
        return ''.join(s)
        
a=Solution2()
print a.reverseVowels("hello")
print a.reverseVowels("leetcode")