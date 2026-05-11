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
        return (self.getCommonLongest(self.generateSubsequence(text1), 
        self.generateSubsequence(text2)))