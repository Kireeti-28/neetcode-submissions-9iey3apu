class Solution:
    def bfs(self, r, c, grid, visited):
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        queue.append((r, c))
        visited.add((r,c))

        perimeter = 0

        while len(queue) > 0:
            cr, cc = queue.popleft()

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for direction in directions:
                dcr, dcc = cr + direction[0], cc + direction[1]

                if (dcr < 0 or dcr >= ROWS or dcc < 0 or dcc >= COLS):
                    perimeter += 1
                elif grid[dcr][dcc] == 0:
                    perimeter += 1
                elif (dcr, dcc) not in visited:
                    visited.add((dcr, dcc))
                    queue.append((dcr, dcc))
        
        return perimeter
            
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return self.bfs(r, c, grid, set())