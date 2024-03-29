class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        buy = prices[0]
        for i in range(n):
            if buy > prices[i]:
                buy = prices[i]
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
                
        