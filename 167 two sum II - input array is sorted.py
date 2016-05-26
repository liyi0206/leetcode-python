class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1,p2=0,len(numbers)-1
        while p1<p2:
            if numbers[p1]+numbers[p2]==target: return (p1+1,p2+1)
            elif numbers[p1]+numbers[p2]<target:p1+=1
            else: p2-=1
        return (-1,-1) 
            
a=Solution()
print a.twoSum([2,7,11,15],9)