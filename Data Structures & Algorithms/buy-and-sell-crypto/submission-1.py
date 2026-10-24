class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        lowest_price = prices[0]
        for price in prices:
            if price > lowest_price:
                profit = max(profit, price - lowest_price)
            else:
                lowest_price = price
        return profit