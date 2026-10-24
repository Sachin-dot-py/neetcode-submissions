from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() # of (i, j) coordinates of seen land
        islands = 0
        m, n = len(grid), len(grid[0])
        # Multi-source DFS
        # Start at each land to be discovered
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    # Found a new island, fully discover this one.
                    islands += 1
                    stack = deque()
                    stack.append((i, j))
                    while stack:
                        i, j = stack.pop()
                        seen.add((i, j))
                        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n:
                                if grid[ni][nj] == "1" and (ni, nj) not in seen:
                                    stack.append((ni, nj))
        return islands
        
