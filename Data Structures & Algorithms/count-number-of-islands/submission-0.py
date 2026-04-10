class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0'):
                return
            
            if ((r, c) in visited):
                return
            
            visited.add((r, c))

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

            return
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and grid[r][c] == '1'):
                    dfs(r, c)
                    islands += 1
        
        return islands