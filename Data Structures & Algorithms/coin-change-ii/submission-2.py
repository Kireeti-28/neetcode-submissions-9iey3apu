class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i, amount):
            if i >= len(coins):
                return 0
            
            if amount == 0:
                return 1
            
            if amount < 0:
                return 0


            return dfs(i, amount - coins[i]) + dfs(i + 1, amount - coins[i])
        
        return dfs(0, amount)