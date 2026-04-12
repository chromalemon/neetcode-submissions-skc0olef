class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[mid-1]:
                break
            else:
                right = mid-1
        if target <= nums[-1]:
            left, right = mid, len(nums)-1
        else:
            left, right = 0, mid-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid
        return -1
