class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if l == r:
                return 1
            
            if (l, r) in memo:
                return memo[(l,  r)]
            
            if s[l] == s[r]:
                memo[(l, r)] = 2 + dfs(l + 1, r - 1)
            else:
                memo[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            
            return memo[(l, r)]
        
        return dfs(0, len(s) - 1)

        