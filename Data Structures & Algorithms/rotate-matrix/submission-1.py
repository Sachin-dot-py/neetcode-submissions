class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose and then reverse rows
        # Step 1: Transpose in-place
        # ALWAYS REMEMBER TO SWAP BOTH NOT JUST ONE SIDE
        s = len(matrix)
        for i in range(s):
            for j in range(i + 1, s):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse rows
        for row in range(s):
            matrix[row].reverse()
        