class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        perimeter = 0

        queue = deque([])
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))
        

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) > 0:
            cr, cc = queue.popleft()

            for dr, dc in directions:
                cdr, cdc = cr + dr, cc + dc

                if (cdr, cdc) in visited:
                    continue

                if cdr >= ROWS or cdr < 0 or cdc >= COLS or cdc < 0 or grid[cdr][cdc] == 0:
                    perimeter += 1
                    continue
                
                visited.add((cdr, cdc))
                queue.append((cdr, cdc))
        
        return perimeter

