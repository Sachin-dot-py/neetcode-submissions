class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, index):
            if index == len(word):
                return True

            if min(i, j) < 0 or i >= len(board) or j >= len(board[0]) or \
                word[index] != board[i][j] or board[i][j] == "#":
                return False

            board[i][j] = "#"
            res = backtrack(i + 1, j, index + 1) or \
                backtrack(i, j + 1, index + 1) or \
                backtrack(i - 1, j, index + 1) or \
                backtrack(i, j - 1, index + 1)
            board[i][j] = word[index]

            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False