class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, visited):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return True
            
            if (board[r][c] == 'X' or (r,c) in visited):
                return False
            
            visited.add((r,c))

            return dfs(r + 1, c, visited) or dfs(r - 1, c, visited) or dfs(r, c + 1, visited) or dfs(r, c - 1, visited)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    if not dfs(r, c, set()):
                        board[r][c] = 'X'
        