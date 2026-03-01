# Iterative Solution:
class Solution1():
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        perimeter = 0

        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == 1:
                    perimeter += 4

                    if row > 0 and grid[row - 1][column] == 1:
                        perimeter -= 2
                    
                    if column > 0 and grid[row][column - 1] == 1:
                        perimeter -= 2
                
        return perimeter


# Depth First Solution:
class Solution2:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(row, column):
            
            if (row < 0 or row == numberOfRows or
                column < 0 or column == numberOfColumns or
                grid[row][column] == 0
            ):
                return 1
            elif (row, column) in visited:
                return 0
            else:
                visited.add((row, column))
                return dfs(row + nr, column + nc) for nr. nc in directions


        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == 1:
                    return dfs(row, column)
        
        return 0


# Breadth First Search
from collections import deque

class Solution3():
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, column):
            queue = deque([(row, column)])
            visited.add((row, column))
            perimeter = 0

            while queue:
                row, column = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = column + dc
                    if (nr < 0 or nr == numberOfRows or
                        nc < 0 or nc == numberOfColumns or
                        grid[nr][nc] == 0
                    ):
                        perimeter += 1
                    elif (nr, nc) in visited:
                        continue
                    else:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return perimeter


        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == 1:
                    return bfs(row, column)
                

        return 0
        

testCases = [
    # Test 1: Large island with hole
    (
        [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ], 30
    ),
    # Test 2: Plus/cross shape
    (
        [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ], 26
    ),
    # Test 3: Checkerboard pattern
    (
        [
            [0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0],
        ], 50
    ),
    # Test 4: All water
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ], 0
    ),
    # Test 5: Single cell
    (
        [[1]], 4  # Fixed: should be 4, not 1
    ),
    # Test 6: Single row (fixed syntax)
    (
        [[1, 0]], 4  # Fixed: removed extra brackets and should be 4
    )
]

solution1 = Solution1()
# Test runner
for i, (grid, expected) in enumerate(testCases):
    result = solution1.islandPerimeter(grid)
    status = "Passed" if result == expected else "Failed"
    print(f"Test {i+1}: {status} Expected {expected}, Got {result}")

print('\n')

solution2 = Solution2()
# Test runner
for i, (grid, expected) in enumerate(testCases):
    result = solution2.islandPerimeter(grid)
    status = "Passed" if result == expected else "Failed"
    print(f"Test {i+1}: {status} Expected {expected}, Got {result}")

print('\n')

solution3 = Solution3()
# Test runner
for i, (grid, expected) in enumerate(testCases):
    result = solution3.islandPerimeter(grid)
    status = "Passed" if result == expected else "Failed"
    print(f"Test {i+1}: {status} Expected {expected}, Got {result}")