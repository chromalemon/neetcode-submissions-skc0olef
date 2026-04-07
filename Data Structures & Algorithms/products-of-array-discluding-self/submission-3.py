class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1]*prefix[i-1])
        for j in range(n-1, -1, -1):
            if j == n-1:
                suffix.append(1)
            else:
                suffix.append(nums[j+1]*suffix[n-j-2])
        res = []
        for k in range(n):
            res.append(prefix[k]*suffix[n-k-1])
        print(prefix)
        print(suffix)
        return res