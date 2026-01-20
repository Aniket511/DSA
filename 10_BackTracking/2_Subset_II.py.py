class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        result = []
        current = []
        nums.sort()

        def backtracking(currentIdx: int) -> None:

            result.append(current[::])

            for idx in range(currentIdx, len(nums)):
                if idx > currentIdx and nums[idx] == nums[idx - 1]:
                    continue
                current.append(nums[idx])
                backtracking(idx + 1)
                current.pop()
        
        backtracking(0)
        return result


# class Solution:
#     def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

#         result = []
#         current = []
#         nums.sort()

#         def backtracking(currentIdx: int) -> None:

#             if currentIdx == len(nums):
#                 result.append(current[::])
#                 return
            
#             current.append(nums[currentIdx])
#             backtracking(currentIdx + 1)
#             current.pop()

#             while currentIdx + 1 < len(nums) and nums[currentIdx] == nums[currentIdx + 1]:
#                 currentIdx += 1
            
#             backtracking(currentIdx + 1)

#         backtracking(0)

#         return result


solution = Solution()

testCases = [
    [1],
    [2,1,2],
    [4,4,4,1,4]
    # [1,2,1,3], 
    # [1,2,3,3,4],
]

for idx, nums in enumerate(testCases):
    result = solution.subsetsWithDup(nums)
    print(f'\nTest Case {idx + 1}, Input: {nums}, Output: {result}')