class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        longest = 0
        seen = {}
        while j <= n-1:
            if s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]] + 1
                seen[s[j]] = j
            else:
                seen[s[j]] = j
            j += 1
            longest = max(longest, j-i)
        return longest
