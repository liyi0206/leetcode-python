class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums,tmp =[],0
        for n in nums:
            tmp +=n
            self.sums.append(tmp)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j]-self.sums[i-1] if i>0 else self.sums[j]


# Your NumArray object will be instantiated and called as such:
a = NumArray([-2, 0, 3, -5, 2, -1])
print a.sumRange(0, 2)
print a.sumRange(2, 5)
print a.sumRange(0, 5)