class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def shell_sort(nums, n):
            gap = n // 2
            while gap >= 1:
                for i in range(gap, n):
                    tmp = nums[i]
                    j = i - gap
                    while j >= 0 and nums[j] > tmp:
                        nums[j + gap] = nums[j]
                        j -= gap
                    nums[j + gap] = tmp
                gap //= 2

        n = len(nums)
        if n == 1:
            return nums
        shell_sort(nums, n)
        return nums


class Solution:
    def sortArray(self, arr: list[int]) -> list[int]:

        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = self.sortArray(arr[:mid])
        right = self.sortArray(arr[mid:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result