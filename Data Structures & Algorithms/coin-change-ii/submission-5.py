class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i, amount):
            if i >= len(coins):
                return 0
            
            if (i, amount) in memo:
                return memo[(i, amount)]

            if amount == 0:
                return 1
            
            if amount < 0:
                return 0


            memo[(i, amount)] = dfs(i, amount - coins[i]) + dfs(i + 1, amount)
        
            return memo[(i, amount)]
            
        memo = {}
        return dfs(0, amount)


        m = len(coins) + 1
        n = amount + 1
        dp = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)

            dp.append(row)

        # i'll have dp intialized

        #base 
        