class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res=[]
        i=0
        while i<len(path):
            if path[i] == "/":
                #print "has /"
                res.append("/")
                i+=1
            elif path[i:i+3]=="../":
                #print "has ../"
                if len(res)>1:
                    res.pop()
                i+=3
            elif path[i:i+2]=="./":
                #print "has ./"
                i+=2
            elif path[i]==".":
                i+=1
            else:
                #print "has letters"
                tmp=path[i]
                i+=1
                while i<len(path) and path[i]!="/":
                    tmp += path[i]
                    i+=1
                if i<len(path) and path[i]=="/": 
                    tmp+="/"
                    i+=1
                res.append(tmp)
                #print res
        #print res
        ret="".join(res).replace("///","/").replace("//",'/')
        return ret[:-1] if len(ret)>1 and ret[-1]=="/" else ret

class Solution:
    def simplifyPath(self, path):
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token == ".." and stack:
                stack.pop()
            elif token != ".." and token != "." and token:
                stack.append(token)
        return "/" + "/".join(stack)