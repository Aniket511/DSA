class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        result = [0] * n
        stack = []
        
        # Iterate from right to left
        for idx in range(n - 1, -1, -1):
            # Count how many people the current person 'idx' can see
            # who are shorter than them
            while stack and heights[idx] > stack[-1]:
                stack.pop()
                result[idx] += 1
            
            # If the stack is not empty, person 'idx' can see the next 
            # taller person who blocked the previous ones
            if stack:
                result[idx] += 1
                
            stack.append(heights[idx])
            
        return result
    
solution = Solution()

print(solution.canSeePersonsCount(heights = [10,6,8,5,11,9]))
print(solution.canSeePersonsCount(heights = [5,1,2,3,10]))