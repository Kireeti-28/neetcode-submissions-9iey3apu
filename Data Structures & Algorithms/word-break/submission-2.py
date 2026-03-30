class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(start_index):
            if (start_index == len(s)):
                return True
            
            if start_index in memo:
                return memo[start_index]
            
            for word in wordDict:
                if (s.startswith(word, start_index)):
                    if (dfs(start_index + len(word))):
                        memo[start_index] = True
                        return True
            
            memo[start_index] = False
            return memo[start_index]
        
        return dfs(0)