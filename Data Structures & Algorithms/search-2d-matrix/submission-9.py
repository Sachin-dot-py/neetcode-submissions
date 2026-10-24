class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            i, j = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True
        return False