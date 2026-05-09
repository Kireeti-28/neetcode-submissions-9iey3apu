class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        [3 2 1]
        [1 1 1]
        [0 -1 1]
        '''
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        grid = []

        for r in range(ROWS):
            row = [0] * COLS
            for c in range(COLS):
                if r == ROWS - 1 and c == COLS - 1:
                    row[c] = 1
                elif obstacleGrid[r][c] == 1:
                    row[c] = -1
            grid.append(row)
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                right = c + 1
                down = r + 1

                rightVal = 0
                downVal = 0

                if right < COLS:
                    rightVal = grid[r][right] if grid[r][right] != -1 else 0
                
                if down < ROWS:
                    downVal = grid[down][c] if grid[down][c] != -1 else 0

                grid[r][c] = grid[r][c] + rightVal + downVal

        return grid[0][0]
