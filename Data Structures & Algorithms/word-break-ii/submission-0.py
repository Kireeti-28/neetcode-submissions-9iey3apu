class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []

        def backtrack(idx, curWords):
            if (idx == len(s)):
                ans.append(' '.join(curWords))
                return
            
            for i in range(len(wordDict)):
                if not s[idx:].startswith(wordDict[i]):
                    continue
                
                curWords.append(wordDict[i])
                backtrack(idx + len(wordDict[i]), curWords)
                curWords.pop()
        
        backtrack(0, [])
        return ans