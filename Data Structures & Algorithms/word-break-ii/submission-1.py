class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordDict = set(wordDict)

        def backtrack(idx, curWords):
            if (idx == len(s)):
                ans.append(' '.join(curWords))
                return
            
            for i in range(idx, len(s)):
                w = s[idx: i + 1]
                if w not in wordDict:
                    continue
                
                curWords.append(w)
                backtrack(i + 1, curWords)
                curWords.pop()
        
        backtrack(0, [])
        return ans