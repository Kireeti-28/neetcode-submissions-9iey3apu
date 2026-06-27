class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
                
            if i == len(s):
                return 1
            
            if i > len(s) or s[i] == '0':
                return 0
            
            if i < len(s) - 1 and int(s[i] + s[i + 1]) > 27:
                return 0
            
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        
        return dfs(0)
            
