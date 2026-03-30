class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(start_index):
            if (start_index == len(s)):
                return True
            
            for word in wordDict:
                if (s.startswith(word, start_index)):
                    if (dfs(start_index + len(word))):
                        return True
            
            return False
        
        return dfs(0)