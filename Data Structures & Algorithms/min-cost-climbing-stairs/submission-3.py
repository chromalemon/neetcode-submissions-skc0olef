class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(n) = min(f(n-1) + cost[n-1], f(n-2) + cost[n-2])

        memo = {}
        memo.update({1: 0, 2: min(cost[0], cost[1])})

        def rec(n):
            if n in memo:
                return memo[n]

            memo[n] = min(rec(n-1) + cost[n-1], rec(n-2) + cost[n-2])

            return memo[n]

        return rec(len(cost))