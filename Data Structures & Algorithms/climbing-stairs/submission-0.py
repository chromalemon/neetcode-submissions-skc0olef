class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n+2)
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.memo[n]