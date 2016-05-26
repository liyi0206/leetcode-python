# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    # reads 4 characters at a time from a file (hard drive).
    # The return value is the actual number of characters read.
    pass

class Solution(object):
    def read(self, buf, n):
        # reads n characters from the file.
        # buf: to be filled by read()
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            buf4 = [""]*4 # a buffer to be filled by read4
            # end of hard drive file, or end of requested length
            cur = min(read4(buf4),n-idx)  
            for i in xrange(cur):
                buf[idx] = buf4[i]
                idx+=1
            # end of hard drive file, or end of requested length
            if cur!=4 or idx==n: return idx


class Solution2(object): #lanlan
    def read(self, buf, n):
        ct=0
        while ct<n:
            tmp = ['']*4
            l = read4(tmp)
            if ct+l<=n:
                buf[ct:ct+l]=tmp[:l]
                ct+=l
            else:
                buf[ct:n]=tmp[:n-ct]
                #self.left = tmp[n-ct:]
                ct=n
            if l<4: break
        return ct