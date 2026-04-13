class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
                