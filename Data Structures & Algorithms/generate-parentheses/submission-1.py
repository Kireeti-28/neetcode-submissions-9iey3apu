class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(s, opens, closes):
            if opens == closes == n:
                ans.append(s[:])
                return
            
            if opens < n:
                backtrack(s + '(', opens + 1, closes)
            if closes < opens:
                backtrack(s + ')', opens, closes + 1)
        
        print(ans)
        backtrack('', 0, 0)
        return ans