class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = deque([])
            queue.append((r, c))
            visited.add((r, c))

            while len(queue) > 0:
                cr, cc = queue.popleft()

                for dr, dc in directions:
                    cdr, cdc = cr + dr, cc + dc

                    if (cdr, cdc) in visited:
                        continue

                    if cdr < 0 or cdr >= ROWS or cdc < 0 or cdc >= COLS or grid[cdr][cdc] == '0':
                        continue
                    
                    visited.add((cdr, cdc))
                    queue.append((cdr, cdc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands