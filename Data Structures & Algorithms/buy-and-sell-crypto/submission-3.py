class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """buy, sell = float("inf"), float("-inf")
        profit = float("-inf")
        for num in prices:
            if num < buy:
                buy = num
                sell = float("-inf")
            elif num > sell:
                sell = num
            profit = max(profit, sell-buy)
        return max(profit, 0)"""
        buy = [float("inf") for _ in range(len(prices)) ] 
        buy[0] = prices[0]
        profit = float("-inf")
        for i in range(1, len(prices)):
            buy[i] = min(prices[i], buy[i-1])
            profit = max(profit, prices[i]-buy[i])
        return max(profit, 0)
