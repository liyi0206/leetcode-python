# -*- coding: utf-8 -*-
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        #"""
        #bulbs=[0]+[1]*n
        #for i in range(2,n+1):
        #    for j in range(1,len(bulbs)):
        #        if j%i==0: bulbs[j]=1-bulbs[j]
        #print bulbs
        #return sum(bulbs) #只有完全平方数的因子个数为奇数
        
        import math
        return int(math.sqrt(n))
        
        
a=Solution()
print a.bulbSwitch(1)
print a.bulbSwitch(2)
print a.bulbSwitch(3)
print a.bulbSwitch(4)
print a.bulbSwitch(5)
print a.bulbSwitch(6)
print a.bulbSwitch(7)
print a.bulbSwitch(8)
print a.bulbSwitch(9)
print a.bulbSwitch(10)
print a.bulbSwitch(11)
print a.bulbSwitch(12)
print a.bulbSwitch(13)
print a.bulbSwitch(14)
print a.bulbSwitch(15)
print a.bulbSwitch(16)
print a.bulbSwitch(17)
print a.bulbSwitch(18)
print a.bulbSwitch(19)
print a.bulbSwitch(20)