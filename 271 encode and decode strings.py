class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(str(len(s))+":"+s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs=[]
        i=0
        while i<len(s):
            j=s.find(':',i)
            i=j+1+int(s[i:j])
            strs.append(s[j+1:i])
        return strs

strs=["hello world!","the sky is blue"]
codec = Codec()
print codec.decode(codec.encode(strs))
#'12:hello world!15:the sky is blue'