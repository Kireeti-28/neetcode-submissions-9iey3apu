class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        out = []

        def addToOut():
            res = []
            for row in board:
                res.append(''.join(row))
            
            out.append(res)

        def makeBoard():
            for i in range(n):
                row = []
                for j in range(n):
                    row.append('.')

                board.append(row)

        def canPlaceQueen(r, c):
            # Row Check
            for cc in range(len(board[r])):
                if board[r][cc] == 'Q':
                    return False
            
            # Column Check
            for rr in range(len(board)):
                if board[rr][c] == 'Q':
                    return False
            
            # Upper Left Diagonal
            rr = r
            cc = c
            for rrr in range(r):
                if rr - 1 >= 0 and cc - 1 >= 0:
                    if board[rr - 1][cc - 1] == 'Q':
                        return False
                
                rr -= 1
                cc -= 1

            # Upper Right Diagonal
            rr = r
            cc = c
            for rrr in range(r):
                if rr - 1 >= 0 and cc + 1 < len(board[0]):
                    if board[rr - 1][cc + 1] == 'Q':
                        return False
                
                rr -= 1
                cc += 1
            
            return True

        def dfs(r, n):
            if n == 0:
                addToOut()
                return
            
            if r >= len(board):
                return
            
            for c in range(len(board[r])):
                if canPlaceQueen(r, c):
                    board[r][c] = 'Q'

                    dfs(r + 1, n - 1)

                    board[r][c] = '.'

        makeBoard()
        dfs(0, n)
        print(out)
        return out
