# -*- coding: utf-8 -*-
class Solution(object):
    #本题与Best Time to Buy and Sell Stock II唯一的区别是
    #在卖出股票后需要间隔至少一天才能再次买入。
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n=len(prices)
        buys,sells = [None]*n,[None]*n 
        buys[0],sells[0] = -prices[0],0
        for x in range(1,n):
            delta=prices[x]-prices[x-1]
            #sells[i]表示在第i天卖出股票所能获得的最大累积收益
            #buys[i]表示在第i天买入股票所能获得的最大累积收益
            
            #max of      #第i-2天卖出~第i天买入的最大累积收益
            buys[x] =max(sells[x-2]-prices[x] if x>1 else None,\
                         #第i-1天买入后反悔~改为第i天买入的最大累积收益
                         buys[x-1] -delta)
            #max of      #第i-1天买入~第i天卖出的最大累积收益
            sells[x]=max(buys[x-1] +prices[x],\
                         #第i-1天卖出后反悔~改为第i天卖出的最大累积收益
                         sells[x-1]+delta)
        return max(sells)
        
    def maxProfit2(self,prices): 
        n=len(prices)
        if n<2: return 0
        buys,sells = [None]*n,[None]*n 
        buys[0],sells[0] =-prices[0],0
        for x in range(1, n):
            #sells[i]表示在第i天不持有股票所能获得的最大累计收益
            sells[x]= max(sells[x-1],buys[x-1] +prices[x])
            #buys[i]表示在第i天持有股票所能获得的最大累计收益
            buys[x] = max(buys[x-1], sells[x-2]-prices[x] if x>1 else -prices[x])
        return sells[-1]
        
        
a=Solution()
print a.maxProfit2([1, 2, 3, 0, 2]) #3
#transactions = [buy, sell, cooldown, buy, sell]