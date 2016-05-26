class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums,self.n =nums,len(nums)
        
        # self.sums is the sume of self value and ++lowbit values.
        # ++lowbit would be larger sibling or parent++ larger sibling.
        self.sums =[0]*(self.n+1)
        for i in xrange(self.n):
            self.add(i+1,nums[i]) # update self.sums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.add(i+1,val-self.nums[i]) # update self.sums
        self.nums[i]=val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums: return 0 # edge case
        return self.sum(j+1)-self.sum(i)
        
        
    ### UTILS ###   
    def lowbit(self,x):
        return x&(-x)
    def add(self,x,val): # for update, idx ++lowbit, sums[idx]+=delta_val
        while x<=self.n: # stop rule x<=n
            self.sums[x]+=val
            x+=self.lowbit(x)
    def sum(self,x):     # for sumRange, idx --lowbit, res+=sums[idx]
        res=0            # stop rule x>0
        while x>0:
            res+=self.sums[x]
            x-=self.lowbit(x)
        return res


nums=[1,3,5]
numArray = NumArray(nums)
print numArray.sumRange(0,2) #9
numArray.update(1,2)
print numArray.sumRange(0,2) #8