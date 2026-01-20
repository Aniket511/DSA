class Solution:
    def exist(self, board, word):

        numberOfRows = len(board)
        numberOfColumns = len(board[0])
        
        def dfs(row, column, idx):
            if idx == len(word):
                return True
            
            if (row < 0 or row == numberOfRows or 
                column < 0 or column == numberOfColumns or
                board[row][column] != word[idx] or
                board[row][column] == '#'):
                return False
            
            board[row][column] = '#'
            
            result = (
                dfs(row + 1, column, idx + 1)
                or dfs(row - 1, column, idx + 1)
                or dfs(row, column + 1, idx + 1)
                or dfs(row, column - 1, idx + 1)
            )
            
            board[row][column] = word[idx]
            return result
        
        for row in range(numberOfRows):
            for column in range(numberOfColumns):
                if board[row][column] == word[0]:
                    if dfs(row, column, 0):
                        return True
        return False


board =[
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
]

solution = Solution()
print(solution.exist(board, 'A'))
print(solution.exist(board, 'ABCDE'))
print(solution.exist(board, 'ABBCDEEFGGFFGHIIIJJKLLKKLMMNNMLKJIHGFEDCBA'))
print(solution.exist(board, 'ABCDEFGHIJKLLLKJIIIIJJKKLMN'))