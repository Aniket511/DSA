# Depth First Solution
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        numberOfRows, numberOfColumns = len(grid), len(grid[0])
        numberOfIslands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= numberOfRows or
                c >= numberOfColumns or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(numberOfRows):
            for c in range(numberOfColumns):
                if grid[r][c] == "1":
                    dfs(r, c)
                    numberOfIslands += 1

        return numberOfIslands

# Breadth First Solution
# from collections import deque 
# class Solution:
#     def numIslands(self, grid: list[list[str]]) -> int:
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         numberOfRows, numberOfColumns = len(grid), len(grid[0])
#         numberOfIslands = 0

#         def bfs(r, c):
#             queue = deque()
#             grid[r][c] = "0"
#             queue.append((r, c))

#             while queue:
#                 row, col = queue.popleft()
#                 for dr, dc in directions:
#                     nr, nc = dr + row, dc + col
#                     if (nr < 0 or nc < 0 or nr >= numberOfRows or
#                         nc >= numberOfColumns or grid[nr][nc] == "0"
#                     ):
#                         continue
#                     queue.append((nr, nc))
#                     grid[nr][nc] = "0"

#         for r in range(numberOfRows):
#             for c in range(numberOfColumns):
#                 if grid[r][c] == "1":
#                     bfs(r, c)
#                     numberOfIslands += 1

#         return numberOfIslands

# Test cases as tuples: (grid, expected_result, description)
testCases = [
    # Test 1: Basic case with one large connected island
    (
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        1
    ),
    
    # Test 2: Multiple separate islands
    (
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        3
    ),
    
    # Test 3: Scattered single-cell islands
    (
        [
            ["1","0","1","0","1"],
            ["0","1","0","1","0"],
            ["1","0","1","0","1"]
        ],
        8
    ),
    
    # Test 4: Single large island covering entire grid
    (
        [
            ["1","1","1"],
            ["1","1","1"],
            ["1","1","1"]
        ],
        1
    ),
    
    # Test 5: No islands, all water
    (
        [
            ["0","0","0"],
            ["0","0","0"]
        ],
        0
    ),
    
    # Test 6: Single cell with land
    (
        [["1"]],
        1
    ),
    
    # Test 7: Single cell with water
    (
        [["0"]],
        0
    ),
    
    # Test 8: Diagonal lands that don't connect
    (
        [
            ["1","0","0"],
            ["0","1","0"],
            ["0","0","1"]
        ],
        3
    ),
    # Test 10: Snake-like winding island
    (
        [
            ["1","0","0","0"],
            ["1","1","0","0"],
            ["0","1","1","0"],
            ["0","0","1","1"]
        ],
        1
    ),
    
    # Test 11: Vertical strip island
    (
        [
            ["1","0","0"],
            ["1","0","0"],
            ["1","0","1"],
            ["1","0","0"]
        ],
        2
    ),
    
    # Test 12: Horizontal strip island
    (
        [
            ["1","1","1","1"],
            ["0","0","0","0"],
            ["0","0","0","0"]
        ],
        1
    ),
    
    # Test 13: Multiple rows with gaps
    (
        [
            ["1","1","0","1","1"],
            ["1","1","0","1","1"],
            ["0","0","0","0","0"],
            ["1","1","0","1","1"]
        ],
        4
    ),
    
    # Test 14: L-shaped island
    (
        [
            ["1","1","0"],
            ["1","0","0"],
            ["1","1","1"]
        ],
        1
    ),
    
    # Test 15: Plus sign shaped island
    (
        [
            ["0","1","0"],
            ["1","1","1"],
            ["0","1","0"]
        ],
        1
    ),
]

solution = Solution()

# Run the tests
print("Running test cases for Number of Islands:\n")
for i, (grid, expected) in enumerate(testCases, 1):
    # Create a deep copy since our function modifies the grid
    grid_copy = [row[:] for row in grid]
    result = solution.numIslands(grid_copy)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i}: {status}")
    print(f"  Expected: {expected}, Got: {result}")
    if result != expected:
        print(f"  MISMATCH!")
    print()