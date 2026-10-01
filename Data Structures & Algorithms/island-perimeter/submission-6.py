class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return 0
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
                return 1
            
            if grid[i][j] == 0:
                return 1

            visited.add((i, j))
            return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        return dfs(0, 0)