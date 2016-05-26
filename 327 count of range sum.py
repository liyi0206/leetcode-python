class Solution(object):
    def countRangeSum(self, nums, lower, upper): #naive o(n^2)
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        sums=[nums[0]]
        for n in nums[1:]: sums.append(sums[-1]+n)
        res=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if lower<=sums[j]-sums[i-1]<=upper: res+=1
        return res
        
class Solution2(object):
    def countRangeSum(self, nums, lower, upper): #o(nlogn) - python sort o(n) TimSort
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.lower,self.upper=lower,upper
        self.first=[0]
        for num in nums: self.first.append(self.first[-1]+num)
        return self.sort(0,len(self.first))
            
    def sort(self,lo, hi):
        mid = (lo+hi)/2
        if mid==lo: return 0
        count=self.sort(lo,mid)+self.sort(mid,hi)
        i=j=mid
        for left in self.first[lo:mid]:
            while i<hi and self.first[i]-left< self.lower: i+=1
            while j<hi and self.first[j]-left<=self.upper: j+=1
            count+=j-i
        self.first[lo:hi] = sorted(self.first[lo:hi])
        return count

class Solution3(object):
    def countRangeSum(self, nums, lower, upper): #BST o(nlogn) - best
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        sums=[nums[0]] #take eg [-2,5,-1]
        for n in nums[1:]: sums.append(sums[-1]+n)
        #print sums #[-2, 3, 2]
        res = 0
        bst = BST()
        for n in reversed(range(len(nums))): 
            # when consider 2 (0,4) in [-2,3], get 3
            # which means we take range [2,2] ([0,2]-[0,1])
            res+=bst.ct(sums[n]+lower,sums[n]+upper) 
            # sums[n]+lower<sums[larger]<sums[n]+upper
            # lower<sums[larger]-sums[n]<upper
            bst.insert(sums[n])
            
        #for n in range(len(nums)): 
        #    res+=bst.ct(sums[n]-upper,sums[n]-lower) 
        #    # sums[n]-upper<sums[i]<sums[n]-lower
        #    # lower<sums[n]-sums[i]<upper
        #    bst.insert(sums[n])
            
        # single sums[n]'s not added yet
        # in the case we add in [0,0], [0,2]
        return res+bst.ct(lower,upper) 
        
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
        self.lct = 0 # left count, including self

class BST:
    def __init__(self):
        self.root = None
     
    def insert(self,val):
        if not self.root: 
            self.root = TreeNode(val)
            self.root.lct = 1
            return
        cur = self.root
        while cur:
            if cur.val<val:
                if not cur.right: 
                    cur.right = TreeNode(val)
                    cur.right.lct = 1
                    return
                cur = cur.right
            else:
                cur.lct+=1
                if not cur.left:
                    cur.left = TreeNode(val)
                    cur.left.lct = 1
                    return
                cur = cur.left
        return
        
    def ct(self,lo,hi):
        return self.ceil(hi)-self.floor(lo)
     
    def ceil(self,val):
        if not self.root: return 0
        cur=self.root
        smaller=0
        while cur:
            if val>=cur.val: ## <=
                smaller+=cur.lct
                cur=cur.right
            else: cur=cur.left
        return smaller # count of smaller elements, including same value ones
             
    def floor(self,val):
        if not self.root: return 0
        cur=self.root
        smaller=0
        while cur:
            if val>cur.val: ## <
                smaller+=cur.lct
                cur=cur.right
            else: cur=cur.left
        return smaller # count of smaller elements, excluding same value ones
        
a=Solution3()
print a.countRangeSum([-2,5,-1],-2,2) #3 - [0,0],[2,2],[0,2]
print a.countRangeSum([0,0],0,0) #3 - [0,0],[0,1],[1,1]

#print a.countRangeSum([2147483647,-2147483648,-1,0],-1,0)
#print a.countRangeSum2([2147483647,-2147483648,-1,0],-1,0)