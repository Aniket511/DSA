class Solution:
    def permuteUnique(self, nums):
        
        nums.sort(reverse = True)

        result = []
        current = []

        used = [False for _ in range(len(nums))]

        def backtracking():

            if len(current) == len(nums):
                result.append(current[::])
                return

            for idx in range(len(nums)):

                if used[idx]:
                    continue

                if idx > 0 and nums[idx] == nums[idx - 1] and not used[idx - 1]:
                    continue
                
                used[idx] = True
                current.append(nums[idx])
                backtracking()

                used[idx] = False
                current.pop()

        backtracking()
        return result

solution = Solution()

testCases = [
    [1,1,2],
    [1,2,2],
    [2,2,2]
]

for idx, nums in enumerate(testCases):
    result = solution.permuteUnique(nums)
    print(f'\nTest Case {idx + 1}, Input: {nums}, Output: {result}')