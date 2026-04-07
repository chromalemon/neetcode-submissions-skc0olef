class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_flag = False
        non_zero_flag = False
        multiple_zeroes_flag = False
        for num in nums:
            if num != 0:
                non_zero_flag = True
                total *= num
            else:
                multiple_zeroes_flag = True if zero_flag else False
                zero_flag = True
        if not non_zero_flag or multiple_zeroes_flag:
            return [0] * len(nums)
        res = []
        for num in nums:
            if num == 0:
                res.append(total)
            else:
                res.append(total//num) if not zero_flag else res.append(0)
        return res