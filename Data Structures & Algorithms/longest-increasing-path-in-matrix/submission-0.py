class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        memo = {}
        def dfs(r, c, prev_val):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev_val:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]

            down = 1 + dfs(r + 1, c, matrix[r][c])
            up = 1 + dfs(r - 1, c, matrix[r][c])
            right = 1 + dfs(r, c + 1,matrix[r][c])
            left = 1 + dfs(r, c - 1, matrix[r][c])

            memo[(r, c)] = max(down, up, right, left)
            return memo[(r, c)]

        maxx = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxx = max(dfs(r, c, -1), maxx)
        
        return maxx