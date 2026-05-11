class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    continue
                
                down = float('inf')
                if r + 1 < ROWS:
                    down = grid[r + 1][c]
                right = float('inf')
                if c + 1 < COLS:
                    right = grid[r][c + 1]
                
                grid[r][c] += min(right, down)
        
        return grid[0][0]
