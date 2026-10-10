class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - buy
            if profit > max_profit:
                max_profit = profit

            if price < buy:
                buy = price
        return max_profit