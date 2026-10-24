class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row = set()
            for num in board[r]:
                if num == ".":
                    continue
                num = int(num)
                if not (0 <= num <= 9):
                    return False
                if num in row:
                    return False
                row.add(num)
        
        for c in range(9):
            column = set()
            for row in board:
                num = row[c]
                if num == ".":
                    continue
                num = int(num)
                if not (0 <= num <= 9):
                    return False
                if num in column:
                    return False
                column.add(num)

        squares = defaultdict(set)
        for r in range(9):
            for c, num in enumerate(board[r]):
                if num == ".":
                    continue
                num = int(num)
                if not (0 <= num <= 9):
                    return False
                if num in squares[(r // 3, c // 3)]:
                    return False
                squares[(r // 3, c // 3)].add(num)
        
        return True