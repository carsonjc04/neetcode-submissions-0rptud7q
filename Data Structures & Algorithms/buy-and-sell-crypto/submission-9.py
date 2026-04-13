class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProft = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                maxProft = max(maxProft, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxProft