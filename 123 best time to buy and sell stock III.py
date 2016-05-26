class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        min_price, max_profit, max_profits = sys.maxint, 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit= max(max_profit,price-min_price)
            max_profits.append(max_profit)
        max_price, max_profit_after, max_combined_profit = 0, 0, 0
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_after = max(max_profit_after, max_price - prices[i])
            max_combined_profit = max(max_combined_profit, \
                                      max_profit_after + max_profits[i])
        return max_combined_profit