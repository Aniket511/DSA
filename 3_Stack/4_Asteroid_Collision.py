class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for size in asteroids:
            while stack and stack[-1] > 0 and size < 0:
                difference = stack[-1] + size
                if difference == 0:
                    stack.pop()
                    size = 0
                elif difference < 0:
                    stack.pop()
                else:
                    size = 0
            if size != 0:
                stack.append(size)
        return stack

solution = Solution()
print(solution.asteroidCollision(asteroids = [5,10,-5]))
print(solution.asteroidCollision(asteroids = [8,-8]))
print(solution.asteroidCollision(asteroids = [10,2,-5]))