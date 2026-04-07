class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = {}
        for index, num in enumerate(nums):
            find = target-num
            if find in ndict:
                i = min(ndict[find], index)
                j = max(ndict[find], index)
                return [i,j]
            if num not in ndict:
                ndict[num] = index

