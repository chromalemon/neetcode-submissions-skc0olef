class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(n) = max( f(n-1), f(n-2) + nums[n] )
        n = len(nums)



        memo = {}

        def rec(n):
            if n <= 0:
                return nums[0]
            if n == 1:
                return nums[1]

            if n in memo:
                return memo[n]

            memo[n] = max(rec(n-1), rec(n-2) + nums[n], rec(n-3) + nums[n])

            return memo[n]

        return max(rec(n-1), rec(n-2))