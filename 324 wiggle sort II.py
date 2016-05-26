class Solution(object):
    def wiggleSort(self, nums): #o(nlogn)
        # nums has dups, need nums[0]<nums[1]>nums[2]<nums[3]...
        # require: odd larger, even smaller ****
        # Can you do it in O(n) time and/or in-place with O(1) extra space? 
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        snums = sorted(nums) 
        for x in range(1,len(nums),2) + range(0,len(nums),2):
            nums[x] = snums.pop()
            
    def wiggleSort2(self,nums): #o(n) ****** quick select ******
        def idx(n):
            # if smaller number(input smaller idx), return odd idx 
            if n<N/2: return 2*n+1 
            
            # if larger number (input larger idx), return even idx
            if n>=N/2: return 2*(n-N/2) 
            
            # when iterate j, from smaller to larger, 
            # aka from odd (left to right) to even (left to right) idx.
            
            # if idx(j) numbers>mid, 
            # switch with num in idx(i), which is in odd idx, from left to right;
            # o/w (<mid) switch with num in idx(k), which is in even idx, from right to left.
            
            # the ones ==mid stay at their locs. they've been changed when i or k
            # locs are replaced with large or small numbers, so they will all be
            # exchanged to odd right, or even left.

        #If find median using quick select instead, it is O(n)
        tmp = sorted(nums)
        N = len(nums)
        mid = tmp[N/2]
        
        i,j,k = 0,0,N-1
        while j<=k:
            if nums[idx(j)]>mid: 
                nums[idx(j)],nums[idx(i)] = nums[idx(i)],nums[idx(j)]
                i,j=i+1,j+1 # odd idx fill from left to right, 
                            # large numbers in first, then median numbers
            elif nums[idx(j)]<mid:
                nums[idx(j)],nums[idx(k)] = nums[idx(k)],nums[idx(j)]
                k-=1        # even idx fill from right to left,
                            # small numbers in first, then median numebrs
            else:j+=1 # there could be several median numbers, 
                      # but should be <N/2
        
a=Solution()
#nums1=[1, 5, 1, 1, 6, 4]
#a.wiggleSort(nums1)
#print nums1

#nums2=[1, 3, 2, 2, 3, 1]
#a.wiggleSort(nums2)
#print nums2

nums3=[1,2,3,3,3,3,4,5]
import random
random.shuffle(nums3); print nums3
a.wiggleSort2(nums3)
print nums3