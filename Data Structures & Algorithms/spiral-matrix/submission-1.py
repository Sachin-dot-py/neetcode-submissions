class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        left = up = 0
        down = n - 1
        right = m - 1
        result = []
        while left <= right and up <= down:
            for j in range(left, right + 1):
                result.append(matrix[up][j])
            up += 1
            
            for i in range(up, down + 1):
                result.append(matrix[i][right])
            right -= 1

            if up <= down:
                for j in range(right, left - 1, -1):
                    result.append(matrix[down][j])
                down -= 1
            
            if left <= right:
                for i in range(down, up - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result