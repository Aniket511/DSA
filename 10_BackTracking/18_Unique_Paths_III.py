class Solution:
    def uniquePathsIII(self, grid):

        numberOfRows = len(grid)
        numberOfColumns = len(grid[0])
        empty_squares = 0
        
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if grid[row][column] == 0:
                    empty_squares += 1
                elif grid[row][column] == 1:
                    start_row, start_col = row, column
        
        self.valid_paths = 0
        
        def dfs(current_row, current_col, remaining_squares):
            if (current_row < 0 or current_col < 0 or 
                current_row >= numberOfRows or current_col >= numberOfColumns or 
                grid[current_row][current_col] == -1):
                return
            
            if grid[current_row][current_col] == 2:
                if remaining_squares == -1:
                    self.valid_paths += 1
                return
            
            original_value = grid[current_row][current_col]
            grid[current_row][current_col] = -1
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for delta_row, delta_col in directions:
                next_row = current_row + delta_row
                next_col = current_col + delta_col
                dfs(next_row, next_col, remaining_squares - 1)
            
            grid[current_row][current_col] = original_value
        
        dfs(start_row, start_col, empty_squares)
        return self.valid_paths

solution = Solution()