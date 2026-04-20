class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while (len(queue) != 0):
            curGridItem = queue.popleft()

            for direction in directions:
                cdr, cdc, cdd = direction[0] + curGridItem[0], direction[1] + curGridItem[1], curGridItem[2] + 1

                if cdr < 0 or cdr >= ROWS or cdc < 0 or cdc >= COLS or grid[cdr][cdc] == -1:
                    continue
                elif grid[cdr][cdc] == 2147483647:
                    grid[cdr][cdc] = cdd
                    queue.append((cdr, cdc, cdd))
        
        return

        