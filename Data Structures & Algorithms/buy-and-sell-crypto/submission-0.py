class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low, high = 0, 1
        while high < len(prices):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]
                max_profit = max(max_profit, profit)
            else:
                low = high
            high += 1
        return max_profit