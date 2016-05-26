class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a,b=None,None
        for n in nums:
            if a is None or n<=a: a=n
            elif b is None or n<=b: b=n
            else: return True
        return False
        
a=Solution()
print a.increasingTriplet([1, 2, 3, 4, 5])
print a.increasingTriplet([5, 4, 3, 2, 1])