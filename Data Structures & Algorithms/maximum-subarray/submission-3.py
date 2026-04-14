class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        maximum = nums[0]
        for num in nums[1:]:
            curr = max(num, num+prev)
            prev = curr
            maximum = max(maximum, curr)
        return maximum
