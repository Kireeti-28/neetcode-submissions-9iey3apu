class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dfs(i, cur_amnt):
            if i >= len(coins) or cur_amnt > amount:
                return 0

            if (i, cur_amnt) in memo:
                return memo[(i, cur_amnt)]

            if cur_amnt == amount:
                return 1

            memo[(i, cur_amnt)] = dfs(i, cur_amnt + coins[i]) + dfs(i + 1, cur_amnt)
            return memo[(i, cur_amnt)]
        
        return dfs(0, 0)