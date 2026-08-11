class Solution:
    def isValid(self, s: str) -> bool:
        opens = '([{'
        closes = ')]}'
        stack = []
        ranks = {
            '(': 1,
            ')': 1,
            '{': 2,
            '}': 2,
            '[': 3,
            ']': 3
        }

        for ss in s:
            if ss in opens:
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                
                
                sss = stack.pop()
                if ranks[sss] != ranks[ss]:
                    return False
        
        return True
                
