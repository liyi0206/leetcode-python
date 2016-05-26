class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res=[]
        counter,tmp=len(words[0]),[words[0]]
        for i in range(1,len(words)):
            if counter+1+len(words[i])<=maxWidth: 
                counter+=1+len(words[i])
                tmp.append(words[i])
            else: 
                res.append(tmp)
                counter,tmp=len(words[i]),[words[i]]
        res.append(tmp)
        #print res
        
        for i in range(len(res)):
            if len(res[i])==1: res[i]=res[i][0].ljust(maxWidth)
            elif i==len(res)-1:res[i]=" ".join(res[i]).ljust(maxWidth)
            else:
                num_spaces=maxWidth-sum([len(w) for w in res[i]])
                num_words=len(res[i])
                space,extra=num_spaces/(num_words-1),num_spaces%(num_words-1)
                tmp=res[i][0]
                for w in res[i][1:]:
                    if extra: 
                        tmp+=" "*space+" "+w
                        extra-=1
                    else: tmp+=" "*space+w
                res[i]=tmp
        return res
        
        
a=Solution()
print a.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print a.fullJustify(["What","must","be","shall","be."], 12)