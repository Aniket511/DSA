class Solution:
    def trap(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        totalWater = 0

        while left <= right:

            if height[left] <= height[right]:

                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    totalWater += leftMax - height[left]
                left += 1

            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    totalWater += rightMax - height[right]
                right -= 1

        return totalWater

solution = Solution()
print(solution.trap(height = [9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9])) # 64
print(solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(solution.trap(height = [4,2,0,3,2,5])) # 9