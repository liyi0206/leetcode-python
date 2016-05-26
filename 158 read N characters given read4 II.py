# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

class Solution(object):
    def __init__(self):
        self.queue = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)
            self.queue.extend(buf4)
            cur = min(len(self.queue), n-idx)
            for i in xrange(cur):
                buf[idx] = self.queue.pop(0)
                idx+=1
            if cur<4 or idx==n: break 
        return idx
        
            
class Solution2(object): #lanlan, WA
    def __init__(self):
        self.left = ""
    
    def read(self, buf, n):
        ct=0
        if len(self.left)>0:
            last = min(len(self.left),n)
            buf[:last] = self.left[:last]
            self.left = self.left[last:]
            ct+=last
            
        while ct<n:
            tmp = ['']*4
            l = read4(tmp)
            if ct+l<=n:
                buf[ct:ct+l]=tmp[:l]
                ct+=l
            else:
                buf[ct:n]=tmp[:n-ct]
                self.left = tmp[n-ct:]
                ct=n
            if l<4: break
        return ct
        
        
#a=Solution()
#a.read("ab"
#[read(1),read(2)])


#"YEiOwYgGGpazYrplFQwkDXCUXHNjTziyCfytblUsRTKuElgBbHbetJZkDAJqQbRHOxTTudiNtBjsyZAmxFkeFBWbFUxsHOcYMtGGIZzwfyeBMvvtAgluXAveQFwHbBzfHjcSaysZgepMqOIuInlKzKMBrWVzYfkZheSFCNakYaQgsWpWkptxLlDFFYjmWFIJgWXxKyISNlbaLKJOWqkHAKnVxAjviPBIStqxkaPZeLAjqBGQldOrmXPoYLjkXSwEZLKoyYIkpGwaDzHknWAwvnKLZZLSwrAmXpUZJvOuAMVcYYxoWWsiKWlpLBiByhqTCJpZwCpvxlBmqYSAiQdCMhABbdBFMEwaqeFsNuHnmNMlXHWyajnBfruZyyhLaYdmELZ"
#[read(374),read(12),read(13)]