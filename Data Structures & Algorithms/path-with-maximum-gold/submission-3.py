class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, gold):
            nonlocal max_gold
            if (i, j) in visited or grid[i][j] == 0:
                return gold
            visited.add((i, j))
            gold += grid[i][j]
            max_gold = max(max_gold, gold)
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    dfs(ni, nj, gold)
            visited.remove((i, j))
                    
            
        max_gold = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        return max_gold

