class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in matrix:
            for idx in range(cols):
                heights[idx] = heights[idx] + 1 if row[idx] == '1' else 0
            
            stack = [-1]
            for idx in range(cols + 1):
                while heights[idx] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = idx - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(idx)
                
        return max_area
    
solution = Solution()
print(solution.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))