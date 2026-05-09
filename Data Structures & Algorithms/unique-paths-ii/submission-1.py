class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
            
        grid = [[0] * COLS for _ in range(ROWS)]
        grid[ROWS - 1][COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    grid[r][c] = 0
                    continue
                
                if r == ROWS - 1 and c == COLS - 1:
                    continue
                
                res = 0
                if r + 1 < ROWS:
                    res += grid[r + 1][c]
                if c + 1 < COLS:
                    res += grid[r][c + 1]
                
                grid[r][c] = res

        return grid[0][0]
