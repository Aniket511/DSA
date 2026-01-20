class Solution:
    def findSubsequences(self, nums):
        result = []
        current = []
        
        def backtracking(currentIdx):
            if len(current) >= 2:
                result.append(current[:])
            
            used = set()
            
            for idx in range(currentIdx, len(nums)):
                if nums[idx] in used:
                    continue
                
                if not current or nums[idx] >= current[-1]:
                    used.add(nums[idx])
                    current.append(nums[idx])
                    backtracking(idx + 1)
                    current.pop()
        
        backtracking(0)
        return result

solution = Solution()
print(solution.findSubsequences([4, 6, 7, 7]))  
print(solution.findSubsequences([4, 4, 3, 2, 1]))  