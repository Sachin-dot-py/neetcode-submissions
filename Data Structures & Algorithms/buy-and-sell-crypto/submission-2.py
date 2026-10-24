class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - bestPrice)
            bestPrice = min(bestPrice, price)
        return maxProfit