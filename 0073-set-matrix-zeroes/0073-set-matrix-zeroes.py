class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_col_has_zero = False

        # 1. Iterate through the matrix to mark zeros
        for r in range(rows):
            # Check if the first column needs to be zeroed later
            if matrix[r][0] == 0:
                first_col_has_zero = True
            
            # Use the first row and first col as markers (starting from col 1)
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, 0, -1):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
            if first_col_has_zero:
                matrix[r][0] = 0