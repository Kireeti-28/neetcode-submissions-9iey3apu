class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(r, c, i, path):
            # print(path, i, word)
            if i == len(word):
                return True

            if r < 0 or r == ROWS or c < 0 or c == COLS or visited[r][c]:
                return False

            if board[r][c] != word[i]:
                return False
            
            visited[r][c] = True
            path += board[r][c]
            
            for direction in directions:
                if dfs(r + direction[0], c + direction[1], i + 1, path[:]):
                    return True
            
                path = path[0 : len(path) - 1]
                visited[r][c] = False
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if (dfs(r, c, 0, '')):
                        return True
        
        return False

