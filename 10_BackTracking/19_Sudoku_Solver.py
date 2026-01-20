class Solution:
    def solveSudoku(self, board):
        
        unsolved = []
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    unsolved.append((i, j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i // 3) * 3 + j // 3].add(board[i][j])

        def backtrack(index):
            if index == len(unsolved):
                return True

            min_candidate = 10
            min_index = index

            for x in range(index, len(unsolved)):
                i, j = unsolved[x]
                box = (i // 3) * 3 + j // 3
                possible = (
                    {"1","2","3","4","5","6","7","8","9"}
                    - row[i] - col[j] - square[box]
                    )
                if len(possible) < min_candidate:
                    min_candidate = len(possible)
                    min_index = x
                if min_candidate == 1:
                    break

            # MRV swap
            unsolved[index], unsolved[min_index] = unsolved[min_index], unsolved[index]

            i, j = unsolved[index]
            box = (i // 3) * 3 + j // 3
            possible_numbers = (
                {"1","2","3","4","5","6","7","8","9"}
                - row[i] - col[j] - square[box]
            )

            for num in possible_numbers:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                square[box].add(num)

                if backtrack(index + 1):
                    return True

                row[i].remove(num)
                col[j].remove(num)
                square[box].remove(num)
                board[i][j] = "."

            unsolved[index], unsolved[min_index] = unsolved[min_index], unsolved[index]
            return False

        backtrack(0)
        for row in range(9):
            print(board[row])

solution = Solution()
solution.solveSudoku(
    [
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
        ['.', '.','.','.','.','.','.','.','.'],
    ]
)