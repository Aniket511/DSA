class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []
        current = []

        def backtracking(currentIdx: int) -> None:

            result.append(current[::])

            for idx in range(currentIdx, len(nums)):
                current.append(nums[idx])
                backtracking(idx + 1)
                current.pop()

        backtracking(0)

        return result


# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
        
#         result = []
#         current = []

#         def backtracking(currentIdx: int) -> None:

#             if currentIdx == len(nums):
#                 result.append(current[::])
#                 return
            
#             current.append(nums[currentIdx])
#             backtracking(currentIdx + 1)
#             current.pop()
#             backtracking(currentIdx + 1)
        
#         backtracking(0)

#         return result

solution = Solution()

testCases = [
    [1],
    [1,2],
    [1,2,3], 
    [1,2,3,4],
]

for idx, nums in enumerate(testCases):
    result = solution.subsets(nums)
    print(f'\nTest Case {idx + 1}, Input: {nums}, Output: {result}')