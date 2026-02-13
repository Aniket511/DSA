class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        left = 0
        right = len(nums)
        
        while left < right:
            correct_index = nums[left] - 1
        
            if nums[left] == left + 1:
                left += 1
        
            elif (
                nums[left] <= left or
                nums[left] > right or
                nums[left] == nums[correct_index]
            ):
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            else:
                nums[left], nums[correct_index] = nums[correct_index], nums[left]
        
        return left + 1