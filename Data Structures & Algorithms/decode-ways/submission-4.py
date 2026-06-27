class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(i):
            if i == len(s):
                return 1
            
            if i > len(s) or s[i] == '0':
                return 0
            
            if i < len(s) - 1 and int(s[i] + s[i + 1]) > 27:
                return 0
            
            return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)
            
