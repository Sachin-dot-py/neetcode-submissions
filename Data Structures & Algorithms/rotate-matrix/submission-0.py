class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # To rotate, we should transpose and reverse
        matrix.reverse()
        nrows = len(matrix)
        for i in range(nrows):
            for j in range(i + 1, nrows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
