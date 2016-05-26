class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 0x for hex, eight 5 in hex means 8*4=32 0101 in binary
        # so only 1 in the odd digit is power of four.
        return num>0 and num&(num-1)==0 and (num & 0x55555555) != 0