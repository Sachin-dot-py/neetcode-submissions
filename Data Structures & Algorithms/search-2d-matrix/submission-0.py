class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_cell(n):
            return matrix[n // len(matrix[0])][n % len(matrix[0])]
        
        low, high = 0, (len(matrix[0]) * len(matrix)) - 1
        while low <= high:
            mid = (low + high) // 2
            if get_cell(mid) == target:
                return True
            elif get_cell(mid) > target:
                high = mid - 1
            elif get_cell(mid) < target:
                low = mid + 1
        return False