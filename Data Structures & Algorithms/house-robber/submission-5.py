class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(n) = max( f(n-1), f(n-2) + nums[n] )
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0],dp[1] = nums[0], nums[1]

        for i in range(2, n):
            skip = dp[i-3] + nums[i] if i > 2 else 0
            dp[i] = max(dp[i-1], dp[i-2] + nums[i], skip)

        return max(dp[n-1], dp[n-2])