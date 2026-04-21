class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific_visited = set()
        pacific_queue = deque([])
        for r in range(1):
            for c in range(COLS):
                pacific_visited.add((r, c))
                pacific_queue.append((r, c))
        
        for r in range(ROWS):
            for c in range(1):
                pacific_visited.add((r, c))
                pacific_queue.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while (len(pacific_queue) != 0):
            cr, cc = pacific_queue.popleft()

            for dr, dc in directions:
                cdr, cdc = dr + cr, dc + cc

                if cdr < 0 or cdr >= ROWS or cdc < 0 or cdc >= COLS or heights[cdr][cdc] < heights[cr][cc]:
                    continue
                elif (cdr, cdc) not in pacific_visited:
                    pacific_visited.add((cdr, cdc))
                    pacific_queue.append((cdr, cdc))

        atlantic_visited = set()
        atlantic_queue = deque([])

        for r in range(ROWS-1, ROWS):
            for c in range(COLS):
                atlantic_queue.append((r, c))
                atlantic_visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS - 1, COLS):
                atlantic_queue.append((r, c))
                atlantic_visited.add((r, c))
        
        while (len(atlantic_queue) != 0):
            cr, cc = atlantic_queue.popleft()

            for dr, dc in directions:
                cdr, cdc = dr + cr, dc + cc

                if cdr < 0 or cdr >= ROWS or cdc < 0 or cdc >= COLS or heights[cdr][cdc] < heights[cr][cc]:
                    continue
                elif (cdr, cdc) not in atlantic_visited:
                    atlantic_visited.add((cdr, cdc))
                    atlantic_queue.append((cdr, cdc))
        
        ans = []
        for pcell in pacific_visited:
            if pcell in atlantic_visited:
                ans.append(list(pcell))
        
        return ans


        

        

        

        
