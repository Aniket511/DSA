class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        largest_area = 0
        for idx in range(len(heights) + 1):
            while stack and (idx == len(heights) or heights[stack[-1]] >= heights[idx]):
                height = heights[stack.pop()]
                width = idx if not stack else idx - stack[-1] - 1
                largest_area = max(largest_area, height * width)
            stack.append(idx)
        return largest_area