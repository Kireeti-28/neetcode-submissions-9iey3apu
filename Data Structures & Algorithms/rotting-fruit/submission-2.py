class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])

        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minTime = 0
        while (len(queue) != 0):
            cr, cc, ct = queue.popleft()

            for dr, dc in directions:
                cdr, cdc, cdt = cr + dr, cc + dc, ct + 1

                if (cdr < 0 or cdr >= ROWS or cdc < 0 or cdc >= COLS or grid[cdr][cdc] != 1):
                    continue
                elif grid[cdr][cdc] == 1:
                    grid[cdr][cdc] = 2
                    queue.append((cdr, cdc, cdt))
                    minTime = cdt
                    fresh -= 1
            
        return minTime if fresh == 0 else -1