class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}
        maximum = 1
        for num in nums:
            seen[num] = 1
        for num in nums:
            if num-1 not in seen:
                curr = num
                length = 0
                while curr in seen:
                    print(curr)
                    length += 1
                    curr += 1
                maximum = max(maximum, length)
        return maximum