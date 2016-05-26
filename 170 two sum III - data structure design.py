class TwoSum(object):
    # Trade off in this problem should be considered
    # if need to add fast, use array to hold numbers
    # if need to find fast,use hashmap to hold numbers
    def __init__(self):
        """
        initialize your data structure here
        """
        self.mp={}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.mp: self.mp[number]+=1
        else: self.mp[number]=1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.mp:
            j = value-i
            if i==j and self.mp[i]>1 or i!=j and j in self.mp: return True
        return False
        
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
print twoSum.find(4) #True
print twoSum.find(7) #False