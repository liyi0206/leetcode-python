class Solution(object):
    def reverseWords(self, s): #naive
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s[:] = list(' '.join(reversed(''.join(s).split(' '))))
        
    def reverseWords2(self,s): #in place - rotate array
        #reverse each word, reverse whole array
        cur=[]
        flag=0
        s.append(" ")
        for i in range(len(s)):
            if s[i]!=" ": cur.append(s[i])
            else: 
                s[flag:i]=self.myReverse(s[flag:i])
                flag=i+1
        s.pop()
        s=self.myReverse(s)
        
    def myReverse(self,s):  
        n=len(s)   
        for i in range(n/2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
        return s
   
s=list("the sky is blue")         
a=Solution()
a.reverseWords2(s)
print s