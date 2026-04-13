class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        longest = 0
        seen = defaultdict(int)
        while j <= n-1:
            if seen[s[j]] > 0:
                while s[i] != s[j] and i < j-1:
                    seen[s[i]] -= 1
                    i += 1
                i += 1
            else:
                seen[s[j]] = 1  
            j += 1
            longest = max(longest, j-i)
        return longest
