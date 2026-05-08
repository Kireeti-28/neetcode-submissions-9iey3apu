class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cnt = 0
        visited = set()
        def dfs(r, c):
            nonlocal cnt
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if r == m - 1 and c == n - 1:
                cnt += 1
            
            if (r,c) in visited:
                return
            
            visited.add((r, c))

            dfs(r, c + 1)
            dfs(r + 1, c)

            visited.remove((r, c))
        
        dfs(0, 0)
        return cnt
