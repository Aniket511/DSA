class Solution:
    def totalNQueens(self, n: int) -> int:
        
        usedColumns = set()
        positiveDiagonal = set()
        negativeDiagonal = set()

        self.count = 0

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtracking(row):

            if row == n:
                self.count += 1
            
            for column in range(n):
                if (column in usedColumns or
                    (row - column) in negativeDiagonal or
                    (row + column) in positiveDiagonal):
                    continue
                usedColumns.add(column)
                positiveDiagonal.add((row + column))
                negativeDiagonal.add((row - column))
                board[row][column] = 'Q'

                backtracking(row + 1)

                usedColumns.remove(column)
                positiveDiagonal.remove((row + column))
                negativeDiagonal.remove((row - column))
                board[row][column] = '.'

        backtracking(0)

        return self.count

solution = Solution()
print(solution.totalNQueens(8))