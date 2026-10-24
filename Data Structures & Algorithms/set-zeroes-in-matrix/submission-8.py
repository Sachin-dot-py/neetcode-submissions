class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # We will save all the rows to be zeroes in row 0 and col 0
        # First, check if row 0 and col 0 will also need to be zeroed completely
        m, n = len(matrix), len(matrix[0])
        zero_first_row = False
        for i in range(n):
            if matrix[0][i] == 0:
                zero_first_row = True
                break
        zero_first_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                zero_first_col = True
                break

        # Now, go through all rows and columns and set the appropriate row/col to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Now, set all the rows/cols with 0 set in first col/row to 0's
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                
        # Now, set all the first rows and cols to zeros if needed
        if zero_first_row:
            for j in range(n):
                matrix[0][j] = 0
        if zero_first_col:
            for i in range(m):
                matrix[i][0] = 0
        