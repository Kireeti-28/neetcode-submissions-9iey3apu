class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp_solve():
            n = len(coins)
            dp = [[0] * (amount + 1) for _ in range(n + 1)]

            for i in range(n + 1):
                dp[i][0] = 1
            
            for i in range(1, n + 1):
                for j in range(1, amount + 1):
                    dp[i][j] = dp[i - 1][j]

                    if j >= coins[i - 1]:
                        dp[i][j] += dp[i][j - coins[i - 1]]
            
            return dp[n][amount]

        return dp_solve()
        
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
        
        # return dfs(0, 0)