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
