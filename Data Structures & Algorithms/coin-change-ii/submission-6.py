class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i, curAmnt):
            if i >= len(coins):
                return 0

            if curAmnt > amount:
                return 0
            
            if (i, curAmnt) in memo:
                return memo[(i, curAmnt)]

            if curAmnt == amount:
                return 1
            

            memo[(i, curAmnt)] = dfs(i, curAmnt + coins[i]) + dfs(i + 1, curAmnt)
            # print((i, amount))
        
            return memo[(i, curAmnt)]
            
        memo = {}
        # return dfs(0, 0)

        dp = []

        for i in range(len(coins) + 1):
            row = []
            for j in range(sum(coins) + 1):
                if j == amount:
                    row.append(1)
                else:
                    row.append(0)
            dp.append(row)
        

        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount - 1, -1, -1):
                dp[i][j] = dp[i][j + coins[i]] + dp[i + 1][j]
        print(dp)
        return dp[0][0]