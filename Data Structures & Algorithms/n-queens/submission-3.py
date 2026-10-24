class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def legalPosition(i, j):
            if horizontals[i] or verticals[j]:
                return False
            if diagonals[j - i + n - 1] or antidiagonals[i + j]:
                return False
            return True

        def backtrack(chessboard, numqueens):
            if numqueens == n:
                res.append(chessboard[:])
                return
            i = numqueens
            for j in range(n):
                if legalPosition(i, j):
                    horizontals[i] = True
                    verticals[j] = True
                    diagonals[j - i + n - 1] = True
                    antidiagonals[i + j] = True

                    row = list(chessboard[i])
                    row[j] = 'Q'
                    chessboard[i] = "".join(row)

                    backtrack(chessboard, numqueens + 1)

                    row = list(chessboard[i])
                    row[j] = '.'
                    chessboard[i] = "".join(row)

                    horizontals[i] = False
                    verticals[j] = False
                    diagonals[j - i + n - 1] = False
                    antidiagonals[i + j] = False
                    

        res = []
        chessboard = ["." * n] * n
        verticals = [False] * n
        horizontals = [False] * n
        diagonals = [False] * (2*n-1)
        antidiagonals = [False] * (2*n-1)
        backtrack(chessboard, 0)
        return res

# diagonal 0: r = c + (n - 1)
# diagonal 1: r = c + (n - 2)
# diagonal 2: r = c + (n - 3)
# n = 
# r = c + (n - diagNum - 1)


# n = 2
# xx
# xx
            # diagonal 0: (1, 0) = r = c + 1
            # diagonal 1: (0, 0 and 1, 1) > r = c
            # diagonal 2: (0, 1) r = c - 1
# n = 3
# xxx
# xxx
# xxx
# diagonal 0: (2, 0) -> r = c + 2
# diagonal 1: (1, 0 and 2, 1) => r = c + 1
# diagonal 2: (0, 0), (1, 1), (2, 2) => r = c
# diagonal 3: (0, 1), (1, 2) => r = c - 1
# diagonal 4: r = c - 2
# antidiagonal 0: (0, 0) -> r + c = 0
# antidiagonal 1: (1, 0), (0, 1) => r + c = 1
# antidiagonal 2: (2, 0), (1, 1), (0, 2) => r + c = 2
# antidigonal 3: (2, 1), (1, 2),
# antidiagonal 4: (2, 2) 