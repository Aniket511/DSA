class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        self.matrix_sum = [[0 for _ in range(number_of_columns + 1)] for _ in range(number_of_rows + 1)]
        
        for row in range(1, number_of_rows + 1):
            running_sum = 0
            for column in range(1, number_of_columns + 1):
                running_sum += matrix[row - 1][column - 1]
                above = self.matrix_sum[row - 1][column]
                self.matrix_sum[row][column] = running_sum + above
        print(self.matrix_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1 
        row2 += 1
        col1 += 1
        col2 += 1
        top_left = self.matrix_sum[row1 - 1][col1 - 1]
        top_right = self.matrix_sum[row1 - 1][col2]
        bottom_left = self.matrix_sum[row2][col1 - 1]
        bottom_right = self.matrix_sum[row2][col2]
        return bottom_right + top_left - top_right - bottom_left