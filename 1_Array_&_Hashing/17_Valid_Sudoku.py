class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        sub_matrix = [0] * 9

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                current_val = int(board[row][column])
                get_bit = 1 << (current_val - 1)
                sub_matrix_index = (row // 3) * 3 + (column // 3)

                if (rows[row] & get_bit or
                    columns[column] & get_bit or
                    sub_matrix[sub_matrix_index] & get_bit 
                    ):
                    return False
                rows[row] |= get_bit
                columns[column] |= get_bit
                sub_matrix[sub_matrix_index] |= get_bit
        
        return True