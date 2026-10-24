class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # Check row i
            seen = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen:
                    return False
                seen.add(board[i][j])

            # Check column i
            seen = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in seen:
                    return False
                seen.add(board[j][i])

            # Check box i
            start_x, start_y = 3*(i // 3), 3*(i % 3)
            seen = set()
            for x in range(start_x, start_x + 3):
                for y in range(start_y, start_y + 3):
                    if board[x][y] != '.' and board[x][y] in seen:
                        return False
                    seen.add(board[x][y])
        return True
