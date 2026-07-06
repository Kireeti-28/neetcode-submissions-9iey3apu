class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parenthesis = []
        def dfs(s):
            if len(s) == 2 * n:
                parenthesis.append(s[:])
                return

            dfs(s + '(')
            dfs(s + ')')
        
        dfs('')

        def validate(s: str) -> bool:
            opens = 0

            for i in s:
                if i == '(':
                    opens += 1
                else:
                    opens -= 1
                
                if opens < 0:
                    return False
            
            return opens == 0
        
        ans = []
        for parenthes in parenthesis:
            if validate(parenthes):
                ans.append(parenthes)

        return ans