class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float("inf"), float("-inf")
        profit = float("-inf")
        for num in prices:
            if num < buy:
                buy = num
                sell = float("-inf")
            elif num > sell:
                sell = num
            profit = max(profit, sell-buy)
        return max(profit, 0)