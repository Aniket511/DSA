class Solution:
    def solveNQueens(self, n: int) -> int:
        
        usedColumns = set()
        positiveDiagonal = set()
        negativeDiagonal = set()

        result = []

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtracking(row):

            if row == n:
                copy = [''.join(row) for row in board]
                result.append(copy)

            for column in range(n):
                if (column in usedColumns or
                    (row + column) in positiveDiagonal or
                    (row - column) in negativeDiagonal):
                        continue
                
                board[row][column] = 'Q'
                usedColumns.add(column)
                positiveDiagonal.add((row + column))
                negativeDiagonal.add((row - column))

                backtracking(row + 1)

                board[row][column] = '.'
                usedColumns.remove(column)
                positiveDiagonal.remove((row + column))
                negativeDiagonal.remove((row - column))

        backtracking(0)

        return result

solution = Solution()
print(len(solution.solveNQueens(8)))