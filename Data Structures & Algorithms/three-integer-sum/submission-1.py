class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for index in range(n):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            num = nums[index]
            target = 0-num
            i = index+1
            j = n-1
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    res.append([num, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
        return res
                