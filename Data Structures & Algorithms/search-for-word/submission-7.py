class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, index):
            if (i, j) in visited or board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if backtrack(ni, nj, index + 1):
                        return True
            visited.remove((i, j))
            return False
            
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

        