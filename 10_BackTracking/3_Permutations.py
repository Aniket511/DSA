class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []

        def backtracking(currentIdx):
            
            if currentIdx == len(nums):
                result.append(nums[::])
                return

            for idx in range(currentIdx, len(nums)):
                nums[idx], nums[currentIdx] = nums[currentIdx], nums[idx]
                backtracking(currentIdx + 1)
                nums[idx], nums[currentIdx] = nums[currentIdx], nums[idx]

        backtracking(0)
        return result

# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:

#         result = []
#         current = []
#         used = [False for _ in range(len(nums))]

#         def backtracking():

#             if len(current) == len(nums):
#                 result.append(current[::])
#                 return
            
#             for idx in range(len(nums)):
#                 if used[idx]:
#                     continue
#                 used[idx] = True
#                 current.append(nums[idx])
#                 backtracking()

#                 used[idx] = False
#                 current.pop()
                
#         backtracking()
#         return result


solution = Solution()

testCases = [
    [1,2,3],
    # [1,2,3,4]
]

for idx, nums in enumerate(testCases):
    result = solution.permute(nums)
    print(f'\nTest Case {idx + 1}, Input: {nums}, Output: {result}')