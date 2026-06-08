class Solution:
    def generateSubsequence(self, text):
        subsequences = []
        
        def dfs(i, curSequence):
            if i >= len(text):
                subsequences.append(curSequence[:])
                return

            dfs(i + 1, curSequence + text[i])
            dfs(i + 1, curSequence)
        
        dfs(0, "")
        return subsequences
    
    def getCommonLongest(self, sequences1, sequences2):
        common = list(set(sequences1) & set(sequences2))
        common.sort(key = lambda x: len(x))
        return len(common[-1])
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp_solve():
            n1 = len(text1)
            n2 = len(text2)
            dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

            for i in range(1, n1 + 1):
                for j in range(1, n2 + 1):
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
        
            return dp[n1][n2]
        
        return dp_solve()

        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if (text1[i] == text2[j]):
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i, j)]
        
        return dfs(0, 0)
