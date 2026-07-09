class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res

        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(i, comb):
            if i == len(digits):
                res.append(''.join(comb))
                return

            for ch in mp[digits[i]]:
                comb.append(ch)
                dfs(i + 1, comb)
                comb.pop()
            
        dfs(0, [])
        return res



        