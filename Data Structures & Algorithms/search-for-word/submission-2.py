class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(r, c, i, path):
            if i == len(word):
                return True

            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return False

            if board[r][c] != word[i]:
                return False
            
            path += board[r][c]
            # print(path)

            for direction in directions:
                if dfs(r + direction[0], c + direction[1], i + 1, path[:]):
                    return True
            
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if (dfs(r, c, 0, '')):
                        return True
        
        return False

